#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv) {
    int data[8][8] = { 0 };

#pragma omp parallel num_threads(4)
    for (int i = 0; i < 8; i++) {
#pragma omp for
        for (int j = 0; j < 8; j++) {
//        #pragma omp ordered
            {
            data[i][j] = omp_get_thread_num();
            printf("%d ", data[i][j]);
}
        }
        printf("\n");
    }

    return 0;
}
