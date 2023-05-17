#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// best case time complexity : O(n*log(n))
// worse case time complexity : O(n^2)
// average case time complexity : O(n*log(n))
double quickSort(int[], int, int);
int partitionArray(int[], int, int);

void main()
{
    int i, j, size = 10000;
    double timeTaken;

    // for random number generation
    time_t t;
    srand((unsigned)time(&t));

    printf("Enter size of array: ");
    scanf("%d", &size);

    int arr[size];

    printf("\nFor %d numbers in array: \n", size);

    for (i = 0; i < size; i++)
    {
        arr[i] = i + 1;
    }
    timeTaken = quickSort(arr, 0, size - 1);
    // pivots have to be such values that always partitions are always evenly (nearly equal) divided
    printf("Best case time: %0.4lf seconds\n", timeTaken);

    for (i = 0, j = size; i < size; i++, j--)
    {
        arr[i] = j;
    }
    timeTaken = quickSort(arr, 0, size - 1);
    // pivot has to be min or max value in array
    printf("Worst case time: %0.4lf seconds\n", timeTaken);

    for (i = 0; i < size; i++)
    {
        arr[i] = (rand() % size);
    }
    timeTaken = quickSort(arr, 0, size - 1);
    printf("Average case time: %0.4lf seconds\n", timeTaken);
}

double quickSort(int arr[], int first, int last)
{
    int i, j;
    clock_t start, end;
    double timeTaken;
    int endPos;

    start = clock();

    if (first < last)
    {
        endPos = partitionArray(arr, first, last);

        quickSort(arr, first, endPos - 1);
        quickSort(arr, endPos + 1, last);
    }

    end = clock();

    timeTaken = (double)(end - start) / CLOCKS_PER_SEC;

    return timeTaken;
}

int partitionArray(int arr[], int first, int last)
{
    int i, j, pivot, temp;
    i = first;
    j = last;
    pivot = first; // no logic for choosing pivot, just take the first element

    while (i < j)
    {
        while (arr[i] <= arr[pivot])
        {
            i++;
        }

        while (arr[j] > arr[pivot])
        {
            j--;
        }

        if (i < j)
        {
            temp = arr[j];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    temp = arr[j];
    arr[j] = arr[pivot];
    arr[pivot] = temp;

    return j;
}