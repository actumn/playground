#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define NUM 100

void swap(int &a, int &b) { 
  int temp;
  temp = a;
  a = b;
  b = temp;
}

int main(int argc, char **argv) {
  int data[NUM][NUM] = { 0 };
  
  omp_set_num_threads(32);

  #pragma omp prallel nowait
  {
    #pragma omp for nowait
    for (int i = 0; i < NUM; i++) {
      for (int j = 0; j < NUM; j++) {
        data[i][j] = i * NUM + j + 1;
      }
    }

    for (int i = 0; i < NUM / 2; i++) {
      #pragma omp for nowait
      for (int j = 0; j < NUM; j++) {
        swap(data[i][j], data[NUM - i - 1][NUM - j - 1]);
      }
    }
  }

  for (int i = 0; i < NUM; i++) {
    for (int j = 0; j < NUM; j++) {
      printf("data[%3d][%3d] = [%3d]\n", i, j, data[i][j]);
    }
  }

  return 0;
}
