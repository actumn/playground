#include <stdio.h>
#include <omp.h>
#include <math.h>

#define MAX 10000
int main(void)
{
	int i = 0;
	float temp = 0.0;
	double Data[4][MAX] = { 0.0 };

	#pragma omp parallel num_threads(4)
	{
		for (i = 0; i < MAX; i++) {
			Data[omp_get_thread_num()][i] = i;
			temp = sqrt(Data[omp_get_thread_num()][i]);
		}
	}

	for (i = 0; i < MAX; i++) {
		printf("Data[0][%2d] = %3.f : Data[1][%2d] = %3.f : ")
	}
	return 0;
}
