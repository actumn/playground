#include <stdio.h>
#include <omp.h>

int main(int argc, char* argv[]) {
	omp_set_nested(1);

	#pragma omp parallel num_threads(2)
	{
		if (omp_get_thread_num() == 0) {
			omp_set_num_threads(4);
		} 
		else {
			omp_set_num_threads(6);
		}

		printf("%d: %d\n", omp_get_thread_num(), omp_get_max_threads());

		#pragma omp parallel
		{
			#pragma omp master
			{
				printf("Inner: %d\n", omp_get_num_threads());
			}
		}

		#pragma omp parallel
		{
			#pragma omp for ordered
			for (int i = 0; i < 15; i++) {
				#pragma omp ordered
				{
					printf("ancestor thread num: %d, thread_num: %d, i: %2d\n",
						omp_get_ancestor_thread_num(omp_get_level() - 1), omp_get_thread_num(), i);
				}
			}
		}
	}

	return 0;
}
