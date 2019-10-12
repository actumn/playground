#include <stdio.h>
#include <memory.h>
#include <omp.h>

void swap(int &a, int &b) {
    int temp = 0;

    printf("thread ID: %d, temp address : %d\n", omp_get_thread_num(), &temp);

    if (a > b) {
      temp = a;
      a = b;
      b = temp;
    }
}

int main(int argc, char** argv)
{
    int number[9] = { 6, 2, 8, 5, 4, 7, 1, 0, 3 };
    int numberCount = 8;
    int i = 0, j = 0;
    double start, end;

    omp_set_num_threads(4);
    start = omp_get_wtime();

    {
      for (i = 0; i < numberCount + 1; i++) {
        printf("i: %d\n", i);
        if (i % 2 == 0) {
          #pragma omp parallel for default(none) shared(number, numberCount) private(j)
          for (j = 0; j < numberCount; j += 2) {
            int thread_id = omp_get_thread_num();
            printf("j: %d\n", j);
            printf("thread_id: %d\n", thread_id);
            swap(number[j], number[j + 1]);

            printf("thread ID: %d, numberCount address : %d\n", omp_get_thread_num(), &numberCount);
          }
        } else {
          #pragma omp parallel for default(none) shared(number, numberCount) private(j)
          for (j = 1; j < numberCount; j += 2) {
            int thread_id = omp_get_thread_num();
            printf("j: %d\n", j);
            printf("thread_id: %d\n", thread_id);
            swap(number[j], number[j + 1]);

            printf("thread ID: %d, numberCount address : %d\n", omp_get_thread_num(), &numberCount);
          }
        }
      }
    }
    end = omp_get_wtime();

    printf("Extime = %f seconds\n", end - start);
    for (i = 0; i < numberCount; i++) {
      printf("%d\n", number[i]);
    }

    return 0;
}
