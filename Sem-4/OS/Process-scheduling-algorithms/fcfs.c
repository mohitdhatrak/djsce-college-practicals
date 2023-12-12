#include <stdio.h>

void main()
{
    int n, bt[20], wt[20], tat[20], avgWt = 0, avgTat = 0, i, j;
    printf("Enter total number of processes (maximum 20): ");
    scanf("%d", &n);

    printf("\nEnter Process Burst Time: \n");
    for (i = 0; i < n; i++)
    {
        printf("P%d: ", i + 1);
        scanf("%d", &bt[i]);
    }

    wt[0] = 0;

    for (i = 1; i < n; i++)
    {
        wt[i] = 0;
        for (j = 0; j < i; j++)
            wt[i] += bt[j];
    }

    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");

    for (i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i];
        avgWt += wt[i];
        avgTat += tat[i];
        printf("nP[%d]tt%dtt%dtt%d", i + 1, bt[i], wt[i], tat[i]);
    }

    avgWt /= i;
    avgTat /= i;
    printf("\nAverage Waiting Time: %d", avgWt);
    printf("\nAverage Turnaround Time: %d", avgTat);
}