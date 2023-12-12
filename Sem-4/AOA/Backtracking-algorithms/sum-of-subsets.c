#include <stdio.h>
#include <stdlib.h>

int count = 1;

int sumOfSubsets(int arr[], int n, int target, int index, int sum, int subSet[])
{
    if (sum == target)
    {
        printf("Solution %d: \t", count++);
        for (int i = 0; i < index; i++)
        {
            printf("%d\t", subSet[i]);
        }
        printf("\n");

        return 1;
    }

    if (index == n)
    {
        return 0;
    }

    subSet[index] = 1;
    sumOfSubsets(arr, n, target, index + 1, sum + arr[index], subSet);

    // BACKTRACK - don't consider current number
    subSet[index] = 0;
    sumOfSubsets(arr, n, target, index + 1, sum, subSet);
}

void main()
{
    int n, target;

    printf("Enter the number of elements in the set: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements of the array: ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter the target sum: ");
    scanf("%d", &target);

    printf("\nElements: \t");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
    printf("\n");

    int subSet[n];
    sumOfSubsets(arr, n, target, 0, 0, subSet); // index, sum -> 0
}