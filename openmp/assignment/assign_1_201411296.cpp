
#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

using namespace std;
const int NUM_COUNT = 50;

void count_sort(int* a)
{
	const int THREAD_COUNT = 4;
	omp_set_num_threads(THREAD_COUNT);

	int count[NUM_COUNT] = { 0 };
	int parallel_count[NUM_COUNT * THREAD_COUNT] = { 0 };
#pragma omp parallel
	{
		const int thread_id = omp_get_thread_num();

#pragma omp for
		for (int i = 0; i < NUM_COUNT; ++i) {
			parallel_count[NUM_COUNT * thread_id + a[i]]++;
		}

#pragma omp for
		for (int i = 0; i < NUM_COUNT; ++i) {
			for (int t = 0; t < THREAD_COUNT; t++) {
				count[i] += parallel_count[NUM_COUNT*t + i];
			}
		}
	}

	int index = 0;
	for (int i = 0; i < NUM_COUNT; ++i) {
		for (int j = 1; j <= count[i]; ++j) {
			a[index] = i;
			index++;
		}
	}
}


int main(int argc, char** argv)
{
	int a[NUM_COUNT] = { 0 };
	for (int i = 0; i < NUM_COUNT; i++) {
		a[i] = rand() % NUM_COUNT;
	}

	printf("Elements are : \n");
	for (int i = 0; i < 50; i++) {
		printf("%2d ", a[i]);
	}
	puts("\n");


	double start = omp_get_wtime();
	count_sort(a);
	double end = omp_get_wtime();

	printf("Extime = %f seconds\n", end - start);


	printf("Sorted elements are : \n");
	for (int i = 0; i < NUM_COUNT; i++) {
		printf("%2d ", a[i]);
	}
	puts("\n");

	return 0;
}
