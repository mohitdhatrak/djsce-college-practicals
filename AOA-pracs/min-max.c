#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// best case time complexity : O(1)
// worse case time complexity : O(n)
// average case time complexity : O(log n)
void minMax(int[], int, int);

int max, min;

void main()
{
    int size, i;

    printf("Enter number of elements in array: ");
    scanf("%d", &size);

    int arr[size];

    for (i = 0; i < size; i++)
    {
        printf("Enter element %d : ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("\nInput array: ");
    for (i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    minMax(arr, 0, size - 1);

    printf("Minimum element in array : %d\n", min);
    printf("Maximum element in array : %d\n", max);
}

void minMax(int arr[], int lower, int higher)
{
    int tempMax, tempMin, middle;

    if (lower == higher)
    {
        max = min = arr[lower];
    }
    else
    {
        if (lower == higher - 1)
        {
            if (arr[lower] < arr[higher])
            {
                min = arr[lower];
                max = arr[higher];
            }
            else
            {
                min = arr[higher];
                max = arr[lower];
            }
        }
        else
        {
            middle = (lower + higher) / 2;

            minMax(arr, lower, middle);
            tempMax = max;
            tempMin = min;
            minMax(arr, middle + 1, higher);

            if (max < tempMax)
                max = tempMax;
            if (min > tempMin)
                min = tempMin;
        }
    }
}