#include <stdio.h>
#include <string.h>

void computeLPS(char pattern[], int lps[])
{
    int len = strlen(pattern);
    int i = 1, j = 0;

    lps[0] = 0;
    while (i < len)
    {
        if (pattern[i] == pattern[j])
        {
            j++;
            lps[i] = j;
            i++;
        }
        else
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                lps[i] = 0;
                i++;
            }
        }
    }
}

void KMP(char text[], char pattern[])
{
    int n = strlen(text);
    int m = strlen(pattern);

    int lps[m];
    computeLPS(pattern, lps);

    int i = 0, j = 0;
    while (i < n)
    {
        if (text[i] == pattern[j])
        {
            i++;
            j++;
        }

        if (j == m)
        {
            printf("Pattern found at index %d\n", i - j);
            j = lps[j - 1];
        }
        else if (i < n && text[i] != pattern[j])
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                i++;
            }
        }
    }
}

void main()
{
    char text[] = "AABAACAADAABAAABAA";
    char pattern[] = "AABA";

    KMP(text, pattern);
}