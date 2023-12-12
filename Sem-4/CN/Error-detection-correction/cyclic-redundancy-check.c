#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char data[20], genPoly[20], crcStr[20], finalCrcStr[20];
int i, j, dataLen;

int n;

void XOR()
{
    for (j = 0; j < n; j++)
    {
        crcStr[j] = (crcStr[j] == genPoly[j]) ? '0' : '1';
    }
}

void CRC()
{
    for (i = 0; i < n; i++) // take first n bits
    {
        crcStr[i] = data[i];
    }

    do
    {
        if (crcStr[0] == '1') // generator polynomial always starts with 1
        {
            XOR();
        }

        for (j = 0; j < n - 1; j++) // replace n - 1 bits of crcStr with +1 position
        {
            crcStr[j] = crcStr[j + 1];
        }

        crcStr[j] = data[i++]; // nth bit is a new bit, then i++
        // i tracks the current bit from data string
    } while (i < dataLen + (n - 1));
}

void receiver()
{
    int flag = 0;

    printf("Enter the received data: ");
    scanf("%s", data);

    CRC();
    if (crcStr[0] == '0')
    {
        for (j = 0; j < n - 1; j++)
        {
            crcStr[j] = crcStr[j + 1];
        }
        crcStr[j] = '\0';
    }
    else
    {
        flag = 1;
    }

    for (i = 0; i < n - 1; i++)
    {
        // Check if any error is detected
        if (crcStr[i] == '1')
        {
            flag = 1;
            break;
        }
    }

    if (flag)
    {
        printf("Error in transmission.\n");
    }
    else
    {
        printf("No error detected.\n");
    }
}

void main()
{
    printf("Enter the data stream to be sent: ");
    scanf("%s", data);
    printf("Enter the generator polynomial: ");
    scanf("%s", genPoly);

    dataLen = strlen(data);
    n = strlen(genPoly);

    printf("Length of generator polynomial is %d\n", n);
    for (i = dataLen; i < dataLen + (n - 1); i++)
    {
        data[i] = '0';
    }
    data[i] = '\0';
    printf("So, the data is appended with %d zeros: %s\n", n - 1, data);

    CRC();
    if (crcStr[0] == '0')
    {
        for (j = 0; j < n - 1; j++)
        {
            crcStr[j] = crcStr[j + 1];
        }
        crcStr[j] = '\0';
    }
    printf("The CRC or the check value for data is: %s\n", crcStr);

    // replacing the n - 1 zeroes with CRC to get final data
    for (i = dataLen; i < dataLen + (n - 1); i++)
    {
        data[i] = crcStr[i - dataLen];
    }
    data[i] = '\0';
    printf("The final data to be sent is: %s\n", data);

    receiver();
}