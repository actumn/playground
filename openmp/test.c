#include <stdio.h>
int main(){
#pragma omp parallel
    printf("Hello!!%i\n");
    return 0;
}

