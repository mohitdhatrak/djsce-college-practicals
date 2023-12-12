#include <stdio.h>

void main()
{
    int size, i;

    printf("Enter stream size: "); // number of total pages
    scanf("%d", &size);

    int incomingStream[size]; // {4, 1, 2, 4, 5}
    printf("Enter each page: ");
    for (i = 0; i < size; i++)
    {
        scanf("%d", &incomingStream[i]);
    }

    int frames = 3; // can be user input

    int pageFaults = 0;
    int m, n;

    int temp[frames];
    for (m = 0; m < frames; m++)
    {
        temp[m] = -1;
    }

    printf("Incoming Frame 1 Frame 2 Frame 3 \n");
    for (m = 0; m < size; m++)
    {
        int s = 0;

        for (n = 0; n < frames; n++)
        {
            if (incomingStream[m] == temp[n])
            {
                s++;
                pageFaults--;
            }
        }
        pageFaults++;

        if ((pageFaults <= frames) && (s == 0))
        {
            temp[m] = incomingStream[m];
        }
        else if (s == 0)
        {
            temp[(pageFaults - 1) % frames] = incomingStream[m];
        }

        printf("\n");
        printf("%d\t", incomingStream[m]);
        for (n = 0; n < frames; n++)
        {
            if (temp[n] != -1)
                printf("  %d\t", temp[n]);
            else
                printf("  - \t");
        }
    }

    double pageFaultRatio = (double)pageFaults / size;
    double pageHitRatio = 1 - pageFaultRatio;

    printf("\n\nTotal Page Faults: %d\n", pageFaults);
    printf("Total Page Hits: %d\n", size - pageFaults);
    printf("Page fault ratio: %0.2lf\n", pageFaultRatio);
    printf("Page hit ratio: %0.2lf\n", pageHitRatio);
}