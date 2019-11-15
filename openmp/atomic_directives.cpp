#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 100

int main(int argc, char** argv) {
  int sum = 0;

  #pragma omp parallel reduction(+:sum)
  {
    int local_sum = 0;

    #pragma omp for
    for (int i = 1; i <= N; i++) {
      local_sum = local_sum + i;
    }
    
    sum = sum + local_sum;
  }

  printf("sum = %d\n", sum);
  return 0;
}
