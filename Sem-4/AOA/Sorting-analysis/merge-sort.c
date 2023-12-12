#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// best case time complexity : O(n*log(n))
// worse case time complexity : O(n*log(n))
// average case time complexity : O(n*log(n))
double mergeSort(int[], int, int);
void merge(int[], int, int, int);

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
    timeTaken = mergeSort(arr, 0, size - 1);
    printf("Best case time: %0.4lf seconds\n", timeTaken);

    for (i = 0, j = size; i < size; i++, j--)
    {
        arr[i] = j;
    }
    timeTaken = mergeSort(arr, 0, size - 1);
    printf("Worst case time: %0.4lf seconds\n", timeTaken);

    for (i = 0; i < size; i++)
    {
        arr[i] = (rand() % size);
    }
    timeTaken = mergeSort(arr, 0, size - 1);
    printf("Average case time: %0.4lf seconds\n", timeTaken);
}

double mergeSort(int arr[], int l, int r)
{
    int i, j;
    clock_t start, end;
    double timeTaken;
    int m;

    start = clock();

    if (l < r)
    {
        m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }

    end = clock();

    timeTaken = (double)(end - start) / CLOCKS_PER_SEC;

    return timeTaken;
}

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int leftArr[n1], rightArr[n2];

    for (i = 0; i < n1; i++)
    {
        leftArr[i] = arr[l + i];
    }
    for (j = 0; j < n2; j++)
    {
        rightArr[j] = arr[m + 1 + j];
    }

    i = 0;
    j = 0;
    k = l;

    while (i < n1 && j < n2)
    {
        if (leftArr[i] <= rightArr[j])
        {
            arr[k] = leftArr[i];
            i++;
        }
        else
        {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}