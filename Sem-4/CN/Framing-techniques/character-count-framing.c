#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sendStream()
{
    int num;
    char str[100], stream[100];

    printf("\nEnter number of data frames to send: ");
    scanf("%d", &num);

    int index = 0;
    for (int i = 0; i < num; i++)
    {
        int len, j;

        printf("Enter data frame %d: ", i + 1);
        scanf("%s", &str);

        len = strlen(str);

        stream[index] = (len + 1) + '0';
        index++;
        for (j = 0; j < len; j++)
        {
            stream[index] = str[j];
            index++;
        }

        if (i == num - 1)
        {
            stream[index] = '\0';
        }
    }

    printf("Stream to be sent: %s\n", stream);
}

void receiveStream()
{
    char str[100], stream[100];

    printf("\nEnter data stream: ");
    scanf("%s", &stream);

    int streamLen = strlen(stream);

    int index = 0, count = 0, frameSize;
    for (int i = 0; i < streamLen; i++)
    {
        if (index == 0)
        {
            frameSize = (int)(stream[i] - '0');
            index++;
            continue;
        }

        if (index < frameSize)
        {
            str[index - 1] = stream[i];
            index++;
        }
        if (index == frameSize)
        {
            str[index - 1] = '\0';
            count++;
            printf("Data in frame %d: %s \n", count, str);
            index = 0;
        }
    }
}

void main()
{
    int choice;

    printf("MENU: \n");
    printf("1. Send stream \n2. Receive stream \n3. Exit \n");

    do
    {
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            sendStream();
            break;

        case 2:
            receiveStream();
            break;

        case 3:
            printf("Program exit...");
            break;

        default:
            printf("Enter a valid choice!\n");
            break;
        }
    } while (choice != 3);
}