#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv) {
    int data[12];

    for (int i = 0; i < 12; i++) {
        data[i] = i;
    }

#pragma omp parallel for num_threads(4) ordered
    for (int i = 0; i < 11; i++) {
//#pragma omp ordered
        {
            data[i] += data[i + 1];
            printf("%d\n", data[i]);
        }
    }

    return 0;
}
