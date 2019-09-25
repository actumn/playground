#include <stdio.h>
#include <memory.h>
#include <omp.h>

#define WIDTH 20
#define HEIGHT 30

int main(int argc, char** argv)
{
    int dotMatrix[HEIGHT][WIDTH];
    memset(dotMatrix, NULL, sizeof(dotMatrix));
    omp_set_num_threads(3);

    #pragma omp parallel
    {
#pragma omp for
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                dotMatrix[i][j] = omp_get_thread_num();// i * WIDTH + j;
            }
        }
    }



    {
        printf("픽셀값 출력\n\n");

        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
              printf("%3d ", dotMatrix[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
