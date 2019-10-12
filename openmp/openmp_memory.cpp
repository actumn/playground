#include <stdio.h>
#include <memory.h>
#include <omp.h>

int main(int argc, char** argv)
{
  float Data[5] = { 1, 2, 3, 4, 5 };
  printf("Serial Area Data: %.1f, %.1f, %.1f, %.1f, %.1f\n", Data[0], Data[1], Data[2], Data[3], Data[4]);

  #pragma omp parallel default(none) private(Data)
  {
    Data[0] = 7;
    Data[1] = 7;
    printf("Serial Area Data: %.1f, %.1f, %.1f, %.1f, %.1f\n", Data[0], Data[1], Data[2], Data[3], Data[4]);
  }

  printf("Serial Area Data: %.1f, %.1f, %.1f, %.1f, %.1f\n", Data[0], Data[1], Data[2], Data[3], Data[4]); 
}
