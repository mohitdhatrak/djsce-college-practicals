#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// best case time complexity : O(n^2)
// worse case time complexity : O(n^2)
// average case time complexity : O(n^2)
double selectionSort(int[], int);

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
    timeTaken = selectionSort(arr, size);
    printf("Best case time: %0.4lf seconds\n", timeTaken);

    for (i = 0, j = size; i < size; i++, j--)
    {
        arr[i] = j;
    }
    timeTaken = selectionSort(arr, size);
    printf("Worst case time: %0.4lf seconds\n", timeTaken);

    for (i = 0; i < size; i++)
    {
        arr[i] = (rand() % size);
    }
    timeTaken = selectionSort(arr, size);
    printf("Average case time: %0.4lf seconds\n", timeTaken);
}

double selectionSort(int arr[], int size)
{
    int i, j, minIndex, temp;
    clock_t start, end;
    double timeTaken;

    start = clock();

    for (i = 0; i < size - 1; i++)
    {
        minIndex = i;

        for (j = i + 1; j < size; j++)
        {
            if (arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }

        if (minIndex != i)
        {
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    end = clock();

    timeTaken = (double)(end - start) / CLOCKS_PER_SEC;

    return timeTaken;
}