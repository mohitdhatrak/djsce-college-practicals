#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// for 7-bit code
// parity bits are in position 2^m where m = 0, 1, 2
// parity bits -> 1, 2, 4
// for P1, take positions having first (rightmost) bit as 1 -> 1, 3, 5, 7
// for P2, take positions having second (middle) bit as 1 -> 2, 3, 6, 7
// for P4, take positions having third (leftmost) bit as 1 -> 4, 5, 6, 7

// for even parity number of 1s need to be even
// for odd parity number of 1s need to be odd

#define EVEN 'E'
#define ODD 'O'

int dataBits[4] = {7, 6, 5, 3};
int parityBits[3] = {4, 2, 1};
// for P1, P2, P4
int bitPositions[4][3] = {{3, 5, 7}, {3, 6, 7}, {}, {5, 6, 7}};

void generateHammingCode(char parity)
{
    char dataStr[4];
    printf("Enter 4-bit data to be sent: ");
    scanf("%s", &dataStr);

    int code[8]; // start from 1st index

    for (int i = 0; i < 4; i++)
    {
        int pos = dataBits[i];
        code[pos] = (int)(dataStr[i] - '0');
        printf("Data bit %d: %d\n", pos, code[pos]);
    }

    if (parity == EVEN) // do XOR of bits
    {
        // int pos = parityBits[0];
        code[1] = (code[3] ^ code[5] ^ code[7]);
        printf("Parity bit %d: %d\n", 1, code[1]);
        code[2] = (code[3] ^ code[6] ^ code[7]);
        printf("Parity bit %d: %d\n", 2, code[2]);
        code[4] = (code[5] ^ code[6] ^ code[7]);
        printf("Parity bit %d: %d\n", 4, code[4]);
    }
    else if (parity == ODD) // do 1 - XOR of bits
    {
        code[1] = 1 - (code[3] ^ code[5] ^ code[7]);
        printf("Parity bit %d: %d\n", 1, code[1]);
        code[2] = 1 - (code[3] ^ code[6] ^ code[7]);
        printf("Parity bit %d: %d\n", 2, code[2]);
        code[4] = 1 - (code[5] ^ code[6] ^ code[7]);
        printf("Parity bit %d: %d\n", 4, code[4]);
    }

    printf("For given data, 7-bit hamming code with %s parity: ", (parity == EVEN ? "even" : "odd"));
    for (int i = 7; i >= 1; i--)
    {
        printf("%d", code[i]);
    }
    printf("\n");
}

void checkHammingCode(char parity)
{
    int flag = 0;
    char codeStr[10];
    printf("Enter 7-bit code: ");
    scanf("%s", &codeStr);

    int code[8]; // start from 1st index

    for (int i = 1; i <= 7; i++)
    {
        int pos = 8 - i;
        code[pos] = (int)(codeStr[i - 1] - '0');
    }

    if (parity == EVEN) // do XOR of bits
    {
        if (code[1] != (code[3] ^ code[5] ^ code[7]))
        {
            printf("Parity bit %d is in error! \n", 1);
            flag = 1;
            code[1] = (code[3] ^ code[5] ^ code[7]);
        }
        if (code[2] != (code[3] ^ code[6] ^ code[7]))
        {
            printf("Parity bit %d is in error! \n", 2);
            flag = 1;
            code[2] = (code[3] ^ code[6] ^ code[7]);
        }
        if (code[4] = (code[5] ^ code[6] ^ code[7]))
        {
            printf("Parity bit %d is in error! \n", 4);
            flag = 1;
            code[4] = (code[5] ^ code[6] ^ code[7]);
        }
    }
    else if (parity == ODD) // do 1 - XOR of bits
    {
        if (code[1] != (1 - (code[3] ^ code[5] ^ code[7])))
        {
            printf("Parity bit %d is in error! \n", 1);
            flag = 1;
            code[1] = 1 - (code[3] ^ code[5] ^ code[7]);
        }
        if (code[2] != (1 - (code[3] ^ code[6] ^ code[7])))
        {
            printf("Parity bit %d is in error! \n", 2);
            flag = 1;
            code[2] = 1 - (code[3] ^ code[6] ^ code[7]);
        }
        if (code[4] = (1 - (code[5] ^ code[6] ^ code[7])))
        {
            printf("Parity bit %d is in error! \n", 4);
            flag = 1;
            code[4] = 1 - (code[5] ^ code[6] ^ code[7]);
        }
    }

    if (flag)
    {
        printf("Correct 7-bit hamming code with %s parity: ", (parity == EVEN ? "even" : "odd"));
        for (int i = 7; i >= 1; i--)
        {
            printf("%d", code[i]);
        }
        printf("\n");
    }
    else
    {
        printf("Given hamming code has no errors! \n");
    }
}

void main()
{
    int choice;
    char parity;

    do
    {
        printf("\nMENU: \n");
        printf("1. Transmission \n2. Reception \n3. Exit \n");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);
        if (choice != 3)
        {
            printf("1. Enter 'E' for even parity \n2. Enter 'O' for odd parity \n");
            printf("\nChoose parity: ");
            scanf(" %c", &parity); // space is needed else it takes prev space in char
        }

        switch (choice)
        {
        case 1:
            generateHammingCode(parity);
            break;

        case 2:
            checkHammingCode(parity);
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