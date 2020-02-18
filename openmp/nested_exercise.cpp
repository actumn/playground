#include <stdio.h>
#include <omp.h>
#include "math.h"

#define MAX 5

int main(int argc, char* argv[]) {
	double data = 2.0;
	#pragma omp parallel num_threads(4)
	{
		#pragma omp sections
		{
			#pragma omp section
			{
				#pragma omp parallel for
				for (int i = 0; i < MAX; i++) {

				}
			}
			
			#pragma omp section
			{

				#pragma omp parallel for
				for (int i = 0; i < MAX; i++) {

				}
			}

			#pragma omp section
			{

				#pragma omp parallel for
				for (int i = 0; i < MAX; i++) {

				}
			} 

			#pragma omp section
			{

				#pragma omp parallel for
				for (int i = 0; i < MAX; i++) {

				}
			}
		}
	}
}
