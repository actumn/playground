#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

#define ROWS 4
#define COLS 1000000

void mxv(float (*matrix_d)[COLS], float* vector, float* result, int nocol, int norow) {
	float local_result = 0.0;
	#pragma omp parallel for num_threads(4) private(local_result)
	for (int y = 0; y < norow; y++) {
		local_result = 0.0;
		for (int x = 0; x < nocol; x++) {
			local_result += matrix_d[y][x] * vector[x];
		}
		result[y] += local_result;
	}
}

int main(void) {
	float matrix[ROWS][COLS], results[ROWS], vec[COLS];
	int i, j = 0;

	double start_time, end_time, elapsed_time;

	for (j = 0; j < ROWS; j++) {
		for (i = 0; i < COLS; i++) {
			matrix[j][i] = (((float)j) * COLS + (float)i) / ((float) 1000.);
		}
	}
	for (i = 0; i < COLS; i++)
		vec[i] = ((float) i) / (float)1000.;
	
	for (i = 0; i < ROWS; i++)
		results[i] = 0.0;

	
	#pragma omp barrier
	start_time = omp_get_wtime();
	mxv(matrix, vec, results, COLS, ROWS);
	end_time = omp_get_wtime();

	for (i = 0; i < ROWS; i++)
		printf("resi=%f\n", results[i]);
	
	printf("Exe, Time = %f msec\n", (end_time - start_time) * 1000.);
	return 0;
}
