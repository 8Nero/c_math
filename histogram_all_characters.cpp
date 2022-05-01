#include <stdio.h>

#define TOTAL_CHARS 128

int main (void)
{
    int c;

    int nchar[TOTAL_CHARS] = {0};

    while ((c = getchar()) != EOF)
        nchar[c] = nchar[c] + 1;

    for(int i=0; i<TOTAL_CHARS; ++i)
    {
        putchar(i);
        
        for(int j=0; j<nchar[i]; ++j)
            putchar('|');
    putchar('\n');
    }
}
