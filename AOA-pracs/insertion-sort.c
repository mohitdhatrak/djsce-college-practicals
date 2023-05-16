#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// best case time complexity : O(n)
// worse case time complexity : O(n^2)
// average case time complexity : O(n^2)
double insertionSort(int[], int);

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
    timeTaken = insertionSort(arr, size);
    printf("Best case time: %0.4lf seconds\n", timeTaken);

    for (i = 0, j = size; i < size; i++, j--)
    {
        arr[i] = j;
    }
    timeTaken = insertionSort(arr, size);
    printf("Worst case time: %0.4lf seconds\n", timeTaken);

    for (i = 0; i < size; i++)
    {
        arr[i] = (rand() % size);
    }
    timeTaken = insertionSort(arr, size);
    printf("Average case time: %0.4lf seconds\n", timeTaken);
}

double insertionSort(int arr[], int size)
{
    int i, j, temp;
    clock_t start, end;
    double timeTaken;

    start = clock();

    for (i = 1; i <= size - 1; i++)
    {
        temp = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > temp)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = temp;
    }

    end = clock();

    timeTaken = (double)(end - start) / CLOCKS_PER_SEC;

    return timeTaken;
}
