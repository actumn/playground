#include <stdio.h>
#include <stdlib.h>

#define DIGITS 32
#define BASE 2

void output(unsigned int n)
{
    int bit[DIGITS] = { 0 };

    for (int i = DIGITS - 1; i >= 0; i--) {
        bit[i] = n % BASE;
        n /= BASE;
    }

    for (int i = 0; i < DIGITS; i++) {
        printf("%d ", bit[i]);
    }

    return;
}

int main()
{
    unsigned int address = 0xAC146434u; // IP address 172.20.100.52
    unsigned int mask = 0xFFFFFFC0u;    // netmask 255.255.255.192 (26 bits)

    unsigned int result;

    output(address);
    printf("\t:IP address\n");

    output(mask);
    printf("\t:netmask\n");

    result = address & mask;
    output(result);
    printf("\t:network address\n");

    mask = ~mask;   // bit reverse

    result = address | mask;
    output(result);
    printf("\t:broadcase address\n");

    return 0;
}
