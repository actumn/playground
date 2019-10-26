#include <stdio.h>
#include <math.h>

#define MAX 10000000

int main(int argc, char** argv) {
    float* data = new float[MAX];

    for (int i = 0; i < MAX; i++) {
        data[i] = i;
    }

#pragma omp parallel
    {
#pragma omp for
        for (int i = 0; i < MAX; i++) {
            data[i] = sqrt(data[i]);
        }

#pragma omp master
        {
            for (int i = 0; i < 5; i++) {
                printf("master data[%d] = %.4f\n", i, data[i]);
            }
        }

#pragma omp for
        for (int i = 0; i < 5; i++) {
            printf("after data[%d] = %.4f\n", i, data[i]);
        }

#pragma omp for
        for (int i = 0; i < MAX; i++) {
            data[i] = log(data[i]);
        }
    }
    delete data;
    return 0;
}
