#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

#define COLS 1024
#define ROWS 1024
#define THREAD_COUNT 8

void mxv(float (*matrix_a)[COLS], float (*matrix_b)[COLS], float (*result)[COLS]) {
	#pragma omp parallel num_threads(THREAD_COUNT)
	{
		int thread_id = omp_get_thread_num();
		for (int segment = 0; segment < COLS / THREAD_COUNT; segment++) {
			int ay = THREAD_COUNT * segment + thread_id;
			// printf("thread: %d, ay: %d\n", thread_id, ay);

			for (int bx = 0; bx < COLS; bx++) {
				float local_result = 0.0;
			
				for (int i = 0; i < ROWS; i++) {
					local_result += matrix_a[ay][i] * matrix_b[i][bx];
				}

				result[ay][bx] = local_result;
			}
		}
	}
}

int main(void) {
	float matrix_a[ROWS][COLS], matrix_b[ROWS][COLS];
	float results[ROWS][COLS] = { 0.0 };

	double start_time, end_time, elapsed_time;

	for (int j = 0; j < ROWS; j++) {
		for (int i = 0; i < COLS; i++) {
			matrix_a[j][i] = (((float)j) * COLS + (float)i) / ((float) 1000.);
			matrix_b[j][i] = (((float)j) * COLS + (float)i) / ((float) 1000.);
		}
	}
	

	#pragma omp barrier
	start_time = omp_get_wtime();
	mxv(matrix_a, matrix_b, results);
	end_time = omp_get_wtime();
	
	printf("Exe, Time = %f msec\n", (end_time - start_time) * 1000.);
	return 0;
}
