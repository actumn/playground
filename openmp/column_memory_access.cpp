#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

#define SIZE 8000

void matrix_double(float(*matrix_d)[SIZE]) {
	#pragma omp parallel
	for (int x = 0; x < SIZE; x++) {
		for (int y = 0; y < SIZE; y++) {
			matrix_d[y][x] = matrix_d[y][x] * 2;
		}
	}
}

int main(void) {
	float matrix[SIZE][SIZE] = { 0.0 };
	double start_time, end_time, elapsed_time;

	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			matrix[i][j] = (((float) i) * SIZE + j) / ((float) 1000.);
		}
	}

	#pragma omp barrier
	start_time = omp_get_wtime();
	matrix_double(matrix);
	end_time = omp_get_wtime();

	printf("\n Exe. Time = %f msec\n", (end_time - start_time) * 1000.);
	return 0;
}

