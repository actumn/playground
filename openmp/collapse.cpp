#include <stdio.h>
#include <omp.h>

using namespace std;

#define MAX 10

int main(int argc, char* argv[]) {
	int count = 0;

	omp_set_num_threads(4);

	#pragma omp parallel shared(count)
	{
		#pragma omp for ordered //collapse(2)
		for (int i = 0; i < MAX; i++) {
			for (int j = 0; j < MAX; j++) {
				#pragma omp atomic
				count += 1;
				#pragma omp ordered
				printf("i*MAX+j : %2d, thread num: %d\n", i*MAX + j, omp_get_thread_num());
			}
		}
	}

	printf("count = %d\n", count);

	return 0;
}
