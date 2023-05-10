#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void FCFS(int requestArr[], int head, int size)
{
    int totalSeek = 0;
    int currentTrack, distance;
    int tempHead = head;

    for (int i = 0; i < size; i++)
    {
        currentTrack = requestArr[i];
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
        printf("%d ", requestArr[i]);
    }
}

void main()
{
    int size, head;

    printf("Enter number of requests: "); // size = 8
    scanf("%d", &size);
    printf("Enter head position: "); // head = 50
    scanf("%d", &head);

    int requestArr[size]; // {176, 79, 34, 60, 92, 11, 41, 114}
    printf("Enter request array: ");
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &requestArr[i]);
    }

    FCFS(requestArr, head, size);

    // answer
    // Total number of seek operations = 510
    // Seek Sequence is 176 79 34 60 92 11 41 114
}