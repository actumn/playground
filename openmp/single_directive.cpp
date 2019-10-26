#include <omp.h>
#include <stdio.h>


int main (int argc, char* argv[]) {
#pragma omp parallel num_threads(4)
    {
        printf("병렬 영역 single 미사용: %d번 thread 동작\n", omp_get_thread_num());
#pragma omp single
        {
            printf("병렬 영역 single 사용: %d번 thread 동작\n", omp_get_thread_num());
        }

        printf("병렬 영역 single 미사용: %d thread 동작\n", omp_get_thread_num());
    }
    return 0;
}
