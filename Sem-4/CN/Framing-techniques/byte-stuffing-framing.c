#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DELIMITER '$'
#define ESCAPE '#'

void sendStream()
{
    int num;
    char str[100], stream[100];

    printf("\nEnter data frame: ");
    scanf("%s", &str);

    stream[0] = DELIMITER; // add start delimiter

    int inputLen = strlen(str);
    int index = 1;

    for (int i = 0; i < inputLen; i++)
    {
        if (str[i] == DELIMITER || str[i] == ESCAPE)
        {
            stream[index] = ESCAPE;
            index++;
        }

        stream[index] = str[i];
        index++;
    }

    stream[index] = DELIMITER; // add end delimiter
    stream[++index] = '\0';

    printf("Stream to be sent: %s\n", stream);
}

void receiveStream()
{
    char str[100], stream[100];

    printf("\nEnter byte stuffed stream: ");
    scanf("%s", &stream);

    int streamLen = strlen(stream);
    int index = 0;

    for (int i = 1; i < streamLen - 1; i++) // skip start and end delimiters
    {
        if (stream[i] == ESCAPE)
        {
            i++;
        }

        str[index] = stream[i];
        index++;
    }

    str[index] = '\0';

    printf("Original data frame: %s\n", str);
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