
#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

using namespace std;

void count_sort(int* a, int n)
{
	const int THREAD_COUNT = 4;
	omp_set_num_threads(THREAD_COUNT);
	
	int count[n] = { 0 };
	int parallel_count[n * THREAD_COUNT] = { 0 };
	#pragma omp parallel
	{
		const int thread_id = omp_get_thread_num();

		#pragma omp for
		for (int i = 0 ; i < n ; ++i ) {
				parallel_count[n * thread_id + a[i]]++;
		}

		#pragma omp for
		for(int i = 0; i < n; ++i) {
			for(int t = 0; t < THREAD_COUNT; t++) {
					count[i] += parallel_count[n*t + i];
			}
		}
	}
	
	int index = 0;
	for (int i = 0; i < n; ++i){
		for (int j = 1; j <= count[i]; ++j){
			a[index] = i;
			index++;
		}
	}
}


int main(int argc, char** argv)
{
	const int NUM_COUNT = 50;
	int a[NUM_COUNT] = { 0 };
	for (int i = 0; i < NUM_COUNT; i++) {
		a[i] = rand() % NUM_COUNT;
	}

	printf("Elements are : \n");
	for (int i = 0; i < 50; i++){
		printf("%2d ", a[i]);
	}
	puts("\n");
	

	double start = omp_get_wtime();
	count_sort(a, NUM_COUNT);
	double end = omp_get_wtime();	

  printf("Extime = %f seconds\n", end - start);


	printf("Sorted elements are : \n");
	for (int i = 0; i < NUM_COUNT; i++){
		printf("%2d ", a[i]);
	}
	puts("\n");

	return 0;
}
 
