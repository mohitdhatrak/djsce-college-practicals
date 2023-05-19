#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sendStream()
{
    int num;
    char str[100], stream[100] = "01111110";
    char pattern[] = "01111110"; // add at beginning and end of stream

    int patternLen = strlen(pattern);

    printf("\nEnter binary bit string: ");
    scanf("%s", &str);

    int count = 0, index = patternLen;
    int inputLen = strlen(str);

    for (int i = 0; i < inputLen; i++)
    {
        if (str[i] == '0')
        {
            count = 0;
        }
        else if (str[i] == '1')
        {
            count++;
        }

        stream[index] = str[i];
        index++;

        if (count == 5) // stuffing 0 after 5 continous 1s
        {
            stream[index] = '0';
            index++;
            count = 0;
        }
    }

    strcat(stream, pattern);

    printf("Stream to be sent: %s\n", stream);
}

void receiveStream()
{
    char str[100], stream[100];

    printf("\nEnter bit stuffed stream: ");
    scanf("%s", &stream);

    char pattern[] = "01111110"; // remove from beginning and end of stream
    int patternLen = strlen(pattern);

    int index = 0, count = 0;
    int streamLen = strlen(stream);

    for (int i = patternLen; i < streamLen - patternLen; i++)
    {
        if (stream[i] == '0')
        {
            count = 0;
        }
        else if (stream[i] == '1')
        {
            count++;
        }

        str[index] = stream[i];
        index++;

        if (count == 5) // remove stuffed 0 after 5 continous 1s
        {
            i++;
        }
    }
    str[index] = '\0';

    printf("Original data: %s\n", str);
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