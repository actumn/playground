#include <stdio.h>

int main (void) {
  int sum = 0, i = 0;
  int Data[1000] = { 0 };

  #pragma omp parallel for
  for (i = 0; i < 1000; i++) {
    Data[i] = i + 1;
  }

  #pragma omp parallel for reduction(+:sum)
  for (i = 0; i < 1000; i++) {
    sum += Data [i];
  }
  printf("Total sum = %d \n", sum);

  return 0;
}