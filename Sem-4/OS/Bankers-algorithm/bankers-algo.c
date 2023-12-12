#include <stdio.h>

void main()
{
    // P0, P1, P2, P3, P4 are the Process names here
    int n, m, i, j, k;

    printf("Enter number of processes: "); // n = 5
    scanf("%d", &n);
    printf("Enter number of resources: "); // m = 3
    scanf("%d", &m);

    int alloc[n][m], max[n][m];
    // Allocation Matrix
    // int alloc[5][3] = {{0, 1, 0},  // P0
    //                    {2, 0, 0},  // P1
    //                    {3, 0, 2},  // P2
    //                    {2, 1, 1},  // P3
    //                    {0, 0, 2}}; // P4
    // MAX Matrix
    // int max[5][3] = {{7, 5, 3},  // P0
    //                  {3, 2, 2},  // P1
    //                  {9, 0, 2},  // P2
    //                  {2, 2, 2},  // P3
    //                  {4, 3, 3}}; // P4
    printf("Enter allocation matrix: \n");
    for (i = 0; i < n; i++)
    {
        printf("Process %d: ", i);
        for (j = 0; j < m; j++)
        {
            scanf("%d", &alloc[i][j]);
        }
    }
    printf("Enter max matrix: \n");
    for (i = 0; i < n; i++)
    {
        printf("Process %d: ", i);
        for (j = 0; j < m; j++)
        {
            scanf("%d", &max[i][j]);
        }
    }

    int avail[m];
    // Available Resources
    // int avail[3] = {3, 3, 2};
    printf("Enter available resources: ");
    for (i = 0; i < m; i++)
    {
        scanf("%d", &avail[i]);
    }

    int need[n][m];
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            need[i][j] = max[i][j] - alloc[i][j];
        }
    }

    int processCompleted = 0, safe[n], processFlag[n];
    for (i = 0; i < n; i++)
    {
        processFlag[i] = 0;
    }

    for (k = 0; k < n; k++) // to ensure we repeat the whole process n times
    {
        for (i = 0; i < n; i++) // i is the current process number
        {
            if (processFlag[i] == 0)
            {
                int flag = 0;
                for (j = 0; j < m; j++)
                {
                    if (need[i][j] > avail[j])
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                {
                    safe[processCompleted] = i; // add to safe sequence
                    processCompleted++;         // update index
                    for (int x = 0; x < m; x++)
                    {
                        avail[x] += alloc[i][x]; // update available
                    }
                    processFlag[i] = 1; // update processes done array
                }
            }
        }
    }

    int flag = 1;
    for (i = 0; i < n; i++) // to check if any process is left
    {
        if (processFlag[i] == 0)
        {
            flag = 0;
            printf("The following system is not safe!");
            break;
        }
    }
    if (flag == 1)
    {
        printf("Following is the SAFE Sequence:\n");
        for (i = 0; i < n - 1; i++)
        {
            printf("P%d -> ", safe[i]);
        }
        printf("P%d", safe[n - 1]);
    }

    // answer
    // P1->P3->P4->P0->P2
}