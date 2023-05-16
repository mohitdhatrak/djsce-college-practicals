#include <stdio.h>
#include <conio.h>
#include <limits.h>

struct process
{
    int name;
    int burst_time;
    int completion_time;
    int arrival_time;
    int turnaround_time;
    int waiting_time;
};

void find_waiting_time(struct process p[], int n)
{
    int rt[n];
    for (int i = 0; i < n; i++)
    {
        rt[i] = p[i].burst_time;
    }

    int complete = 0, t = 0, min = INT_MAX;
    int shortest = 0, finish_time = 0;
    int check = 0;

    printf("\nGantt Chart\n");

    while (complete != n)
    {
        for (int i = 0; i < n; i++)
        {
            if ((p[i].arrival_time <= t) && (rt[i] < min) && (rt[i] > 0))
            {
                min = rt[i];
                shortest = i;
                check = 1;
            }
        }

        if (check == 0)
        {
            t++;
            printf("  |");
            continue;
        }

        rt[shortest]--;

        min = rt[shortest];
        if (min == 0)
        {
            min = INT_MAX;
        }

        if (rt[shortest] == 0)
        {
            complete++;
            check == 0;

            finish_time = t + 1;
            p[shortest].completion_time = finish_time;

            p[shortest].waiting_time = p[shortest].completion_time - p[shortest].burst_time - p[shortest].arrival_time;
            if (p[shortest].waiting_time < 0)
            {
                p[shortest].waiting_time = 0;
            }
        }

        printf("P%d |", shortest);
        t++;
    }
    printf("\n\n");
}

void find_turnaround_time(struct process p[], int n)
{
    for (int i = 0; i < n; i++)
    {
        p[i].turnaround_time = p[i].burst_time + p[i].waiting_time;
    }
}

void find_avg_time(struct process p[], int n)
{
    int total_turnaround_time = 0, total_waiting_time = 0;

    find_waiting_time(p, n);
    find_turnaround_time(p, n);

    for (int i = 0; i < n; i++)
    {
        total_turnaround_time = p[i].turnaround_time + total_turnaround_time;
        total_waiting_time = p[i].waiting_time + total_waiting_time;
    }

    printf("Process\tArrival Time\tBurst Time\tTurnaround Time\tWaiting Time\tCompletion Time\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", p[i].name, p[i].arrival_time, p[i].burst_time, p[i].turnaround_time, p[i].waiting_time, p[i].completion_time);
    }

    printf("\nAverage Turnaround Time = %f", (float)total_turnaround_time / (float)n);
    printf("\nAverage Waiting Time = %f\n", (float)total_waiting_time / (float)n);
}

int main()
{
    int n;
    printf("Enter the number of processes : ");
    scanf("%d", &n);
    printf("\n");
    struct process p[n];

    for (int i = 0; i < n; i++)
    {
        printf("Enter the Arrival time, Burst Time for P%d : ", i);
        p[i].name = i;
        scanf("%d%d", &p[i].arrival_time, &p[i].burst_time);
    }

    find_avg_time(p, n);
}