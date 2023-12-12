#include <stdio.h>

void bubbleSort(int arr[], int n)
{
    int i, j, temp;

    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] < arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void worstFit(int blockSize[], int m, int processSize[], int n, int holeSize[], int sortedBlock[])
{
    int i, j;
    int allocation[n];

    for (i = 0; i < n; i++)
    {
        allocation[i] = -1;
    }

    for (i = 0; i < n; i++) // n -> number of processes
    {
        int worstBlock;
        for (j = 0; j < m; j++) // m -> number of blocks
        {
            if (sortedBlock[j] != -1 && sortedBlock[j] >= processSize[i])
            {
                worstBlock = sortedBlock[j];
                sortedBlock[j] = -1;
                break;
            }
        }
        for (j = 0; j < m; j++) // m -> number of blocks
        {
            if (worstBlock == holeSize[j])
            {
                allocation[i] = j; // memory block assigned to process

                holeSize[j] -= processSize[i]; // reduce available memory in this block

                break; // go to the next process in the queue
            }
        }
    }

    printf("\nProcess No.\tProcess Size\tAllocated Block no.\n");
    for (int i = 0; i < n; i++)
    {
        printf("%i\t\t", i + 1);
        printf("%i\t\t", processSize[i]);
        if (allocation[i] != -1)
            printf("%i", allocation[i] + 1);
        else
            printf("Not Allocated");
        printf("\n");
    }

    printf("\nBlock No.\tBlock Size\tHole Size\n");
    for (int i = 0; i < m; i++)
    {
        printf("%i\t\t", i + 1);
        printf("%i\t\t", blockSize[i]);
        if (holeSize[i] != blockSize[i])
            printf("%i", holeSize[i]);
        else
            printf("Unused block");
        // printf("%i", holeSize[i]);
        printf("\n");
    }
}

void main()
{
    int m, n;

    printf("Enter number of blocks in the memory: "); // m = 5
    scanf("%d", &m);
    printf("Enter number of processes in the input queue: "); // n = 4
    scanf("%d", &n);

    int blockSize[m], processSize[n], holeSize[m], sortedBlock[m];
    printf("Enter each block size: "); // {100, 500, 200, 300, 600}
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &blockSize[i]);
        holeSize[i] = blockSize[i];
        sortedBlock[i] = blockSize[i];
    }
    printf("Enter each process size: "); // {212, 417, 112, 426}
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &processSize[i]);
    }

    bubbleSort(sortedBlock, m);

    worstFit(blockSize, m, processSize, n, holeSize, sortedBlock);
}
