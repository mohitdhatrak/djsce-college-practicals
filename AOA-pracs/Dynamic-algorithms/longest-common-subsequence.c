#include <stdio.h>
#include <string.h>

void LCS(char s1[], char s2[], int m, int n)
{
    int i, j, table[20][20];

    // filling 0's in table, in string length + 1 places
    for (i = 0; i <= m; i++)
        table[i][0] = 0;
    for (i = 0; i <= n; i++)
        table[0][i] = 0;

    // creating the table in bottom-up way
    for (i = 1; i <= m; i++)
    {
        for (j = 1; j <= n; j++)
        {
            if (s1[i - 1] == s2[j - 1])
            {
                table[i][j] = table[i - 1][j - 1] + 1;
            }
            else if (table[i - 1][j] >= table[i][j - 1])
            {
                table[i][j] = table[i - 1][j];
            }
            else
            {
                table[i][j] = table[i][j - 1];
            }
        }
    }

    int index = table[m][n];   // last num is length of LCS
    char lcsString[index + 1]; // +1 for '\0' at the end
    lcsString[index] = '\0';

    i = m; // not m-1, n-1 as table has 1 extra row and column of zeros
    j = n;
    while (i > 0 && j > 0)
    {
        if (s1[i - 1] == s2[j - 1])
        {
            lcsString[index - 1] = s1[i - 1];
            i--;
            j--;
            index--;
        }

        else if (table[i - 1][j] > table[i][j - 1])
            i--;
        else
            j--;
    }

    // Printing the sub sequences
    printf("\nString 1 : %s \nString 2 : %s \n", s1, s2);
    printf("LCS: %s\n", lcsString);
}

void main()
{
    int m, n;
    char s1[20] = "abaaba", s2[20] = "babbab";

    printf("Enter string 1: ");
    gets(s1);
    printf("Enter string 2: ");
    gets(s2);

    m = strlen(s1);
    n = strlen(s2);

    LCS(s1, s2, m, n);
}