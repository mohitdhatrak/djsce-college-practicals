#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define LEFT 1
#define RIGHT 2
#define NUM_OF_TRACKS 199 // can take user input as well

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

int findPosition(int sortArr[], int head, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (head == sortArr[i])
        {
            return i;
        }
    }
}

void CSCAN(int requestArr[], int sortArr[], int head, int size, int direction)
{
    int totalSeek = 0;
    int seekSequence[size + 2]; // as it will have 2 extreme end elements too
    int headPosition = findPosition(sortArr, head, size + 1);

    if (direction == LEFT)
    {
        int index = 0;
        totalSeek = (head - 0) + (NUM_OF_TRACKS - 0) + (NUM_OF_TRACKS - sortArr[headPosition + 1]);

        // half sequence
        for (int i = headPosition - 1; i >= 0; i--)
        {
            seekSequence[index] = sortArr[i];
            index++;
        }
        seekSequence[index] = 0;
        index++;
        seekSequence[index] = NUM_OF_TRACKS;
        index++;
        // remaining half sequence
        for (int i = size + 1; i > headPosition; i--)
        {
            seekSequence[index] = sortArr[i];
            index++;
        }
    }
    else if (direction == RIGHT)
    {
        int index = 0;
        totalSeek = (NUM_OF_TRACKS - head) + (NUM_OF_TRACKS - 0) + (sortArr[headPosition - 1] - 0);

        // half sequence
        for (int i = headPosition + 1; i < size + 1; i++)
        {
            seekSequence[index] = sortArr[i];
            index++;
        }
        seekSequence[index] = NUM_OF_TRACKS;
        index++;
        seekSequence[index] = 0;
        index++;
        // remaining half sequence
        for (int i = 0; i < headPosition; i++)
        {
            seekSequence[index] = sortArr[i];
            index++;
        }
    }

    printf("\nTotal number of seek operations: %d\n", totalSeek);

    printf("Seek Sequence: ");
    for (int i = 0; i < size + 2; i++)
    {
        printf("%d ", seekSequence[i]);
    }
}

void main()
{
    int size, head, direction = 0;

    printf("Enter number of requests: "); // size = 8
    scanf("%d", &size);
    printf("Enter head position: "); // head = 50
    scanf("%d", &head);

    int requestArr[size];  // {176, 79, 34, 60, 92, 11, 41, 114}
    int sortArr[size + 1]; // add head to this as well
    printf("Enter request array: ");
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &requestArr[i]);
        sortArr[i] = requestArr[i];
    }
    sortArr[size] = head;

    bubbleSort(sortArr, size + 1);

    printf("\n1. Enter 1 for left (R -> L)"
           "\n2. Enter 2 for right (L -> R)");
    printf("\nChoose a direction: "); // LEFT
    scanf("%d", &direction);

    switch (direction)
    {
    case 1:
        CSCAN(requestArr, sortArr, head, size, LEFT);
        break;

    case 2:
        CSCAN(requestArr, sortArr, head, size, RIGHT);
        break;

    default:
        printf("Enter a valid value!");
        break;
    }

    // answer
    // Total number of seek operations = 389
    // Seek Sequence is 60 79 92 114 176 199 0 11 34 41
}