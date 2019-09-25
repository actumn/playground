#include <stdio.h>
#include <omp.h>

int main() {
    omp_set_num_threads(8);

    #pragma omp parallel
    {
        printf("Hello!! tid is %d\n", omp_get_thread_num());
    }
    return 0;
}

