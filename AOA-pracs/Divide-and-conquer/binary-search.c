#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// best case time complexity : O(1)
// worse case time complexity : O(log n)
// average case time complexity : O(log n)
double binarySearch(int[], int, int);
void bubbleSort(int[], int);

void main()
{
    int i, j, size = 10000;
    double timeTaken;

    // for random number generation
    time_t t;
    srand((unsigned)time(&t));

    printf("Enter size of array: ");
    scanf("%d", &size);

    int random[size], best[size], worst[size];

    // we make a random array, same for all cases
    printf("\nFor %d numbers in array: \n", size);
    for (i = 0; i < size; i++)
    {
        random[i] = (rand() % size);
        best[i] = random[i];
        worst[i] = random[i];
    }

    timeTaken = binarySearch(best, size, ((size - 1) / 2));
    // when element is found at the middle of the array
    printf("Best case time: %0.4lf seconds\n", timeTaken);

    timeTaken = binarySearch(worst, size, 0);
    // when element is at either of the extreme ends of array
    printf("Worst case time: %0.4lf seconds\n", timeTaken);

    timeTaken = binarySearch(random, size, (rand() % size));
    printf("Average case time: %0.4lf seconds\n", timeTaken);
}

double binarySearch(int arr[], int size, int position)
{
    int i, j;
    clock_t start, end;
    double timeTaken;

    int search, middle;
    int lower = 0, higher = size - 1;

    start = clock();

    bubbleSort(arr, size);
    search = arr[position]; // after sorting we decide search element to get best, worst, average case times

    for (i = 0; higher >= lower; i++)
    {
        middle = (lower + higher) / 2;

        if (arr[middle] == search)
        {
            break; // instead of returning, since we return time
        }
        else if (arr[middle] < search)
        {
            lower = middle + 1;
        }
        else
        {
            higher = middle - 1;
        }
    }

    end = clock();

    timeTaken = (double)(end - start) / CLOCKS_PER_SEC;

    return timeTaken;
}

void bubbleSort(int arr[], int n)
{
    int i, j, temp;

    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}