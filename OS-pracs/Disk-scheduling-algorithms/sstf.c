#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int closestTrack(int requestArr[], int copyArr[], int size, int tempHead)
{
    int position = 0;
    int min = INT_MAX;
    for (int i = 0; i < size; i++)
    {
        int value = abs(copyArr[i] - tempHead);
        if (copyArr[i] != -1 && value < min)
        {
            min = value;
            position = i;
        }
    }

    copyArr[position] = -1;
    return requestArr[position];
}

void SSTF(int requestArr[], int copyArr[], int head, int size)
{
    int totalSeek = 0;
    int currentTrack, distance;
    int tempHead = head;
    int seekSequence[size];

    for (int i = 0; i < size; i++)
    {
        currentTrack = closestTrack(requestArr, copyArr, size, tempHead);
        seekSequence[i] = currentTrack;

        distance = abs(tempHead - currentTrack);

        // increase the total count
        totalSeek += distance;

        // accessed track is now new head
        tempHead = currentTrack;
    }

    printf("\nTotal number of seek operations: %d\n", totalSeek);

    printf("Seek Sequence: ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", seekSequence[i]);
    }
}

int main()
{
    int size, head;

    printf("Enter number of requests: "); // size = 8
    scanf("%d", &size);
    printf("Enter head position: "); // head = 50
    scanf("%d", &head);

    int requestArr[size]; // {176, 79, 34, 60, 92, 11, 41, 114}
    int copyArr[size];
    printf("Enter request array: ");
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &requestArr[i]);
        copyArr[i] = requestArr[i];
    }

    SSTF(requestArr, copyArr, head, size);
}