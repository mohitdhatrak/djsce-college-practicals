#include <stdio.h>
#include <string.h>

#define d 256

void rabinKarp(char pattern[], char text[], int q)
{
    int i, j;
    int n = strlen(text);
    int m = strlen(pattern);

    int h = 1;
    int p = 0, t = 0;

    for (i = 0; i < m - 1; i++)
    {
        h = (h * d) % q;
    }

    for (i = 0; i < m; i++)
    {
        p = (p * d + pattern[i]) % q;
        t = (t * d + text[i]) % q;
    }

    for (i = 0; i <= n - m; i++)
    {
        if (p == t)
        {
            for (j = 0; j < m; j++)
            {
                if (text[i + j] != pattern[j])
                {
                    break;
                }
            }
            if (j == m)
            {
                printf("Pattern found at index %d\n", i);
            }
        }
        if (i < n - m)
        {
            t = (d * (t - text[i] * h) + text[i + m]) % q;
            if (t < 0)
            {
                t = t + q;
            }
        }
    }
}

void main()
{
    char text[] = "AABCCDA";
    char pattern[] = "CCD";

    int q = 13; // random prime used to hash

    rabinKarp(pattern, text, q);
}