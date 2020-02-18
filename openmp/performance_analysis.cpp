#include <stdio.h>
#include <omp.h>
#include "math.h"

int main(int argc, char* argv[]) {
	double data = 2.0;
	#pragma omp parallel num_threads(2)
	{
		#pragma omp sections
		{
			#pragma omp section
			{
				double start_time = omp_get_wtime();
				double log_Data = log(data); 
				double end_time = omp_get_wtime();

				printf("log Exe, Time = %f msec\n", (end_time - start_time) * 1000.);
			}

			#pragma omp section
			{
				#pragma omp parallel num_threads(2)
				{
					#pragma omp sections
					{
						#pragma omp section
						{				
							double start_time = omp_get_wtime();
							double ex_data = ldexp(data, 1);
							double end_time = omp_get_wtime();
							printf("ldexp Exe, Time = %f msec\n", (end_time - start_time) * 1000.);
						}

						#pragma omp section
						{
							double start_time = omp_get_wtime();
							double rt_data = sqrt(data);
							double end_time = omp_get_wtime();
							printf("sqrt Exe, Time = %f msec\n", (end_time - start_time) * 1000.);
						}
					}
				}
			}
		}
	}
}
