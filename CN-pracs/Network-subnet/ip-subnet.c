#include <stdio.h>
#include <string.h>

int octets[4], mask[4] = {0, 0, 0, 0}, subnet[4];

void getSubnetAddress()
{
    int choice = 0;
    printf("Enter 1 to input subnet mask, 0 to consider default mask: ");
    scanf("%d", &choice);

    if (choice == 1)
    {
        printf("Enter the subnet mask (x.x.x.x): ");
        scanf("%d.%d.%d.%d", &mask[0], &mask[1], &mask[2], &mask[3]);
    }

    subnet[0] = octets[0] & mask[0];
    subnet[1] = octets[1] & mask[1];
    subnet[2] = octets[2] & mask[2];
    subnet[3] = octets[3] & mask[3];

    printf("Subnet mask:  %d.%d.%d.%d\n", mask[0], mask[1], mask[2], mask[3]);
    printf("Subnet address:  %d.%d.%d.%d\n", subnet[0], subnet[1], subnet[2], subnet[3]);
}

void main()
{

    printf("Enter the IP address (x.x.x.x): ");
    scanf("%d.%d.%d.%d", &octets[0], &octets[1], &octets[2], &octets[3]);

    if (octets[0] > 0 && octets[0] <= 127)
    {
        printf("Class of IP address : A\n");
        mask[0] = 255;
        getSubnetAddress();
    }
    else if (octets[0] >= 128 && octets[0] <= 191)
    {
        printf("Class of IP address : B\n");
        mask[0] = 255;
        mask[1] = 255;
        getSubnetAddress();
    }
    else if (octets[0] >= 192 && octets[0] <= 223)
    {
        printf("Class of IP address : C\n");
        mask[0] = 255;
        mask[1] = 255;
        mask[2] = 255;
        getSubnetAddress();
    }
    else if (octets[0] >= 224 && octets[0] <= 239)
    {
        printf("Class of IP address : D (multicast)\n");
    }
    else if (octets[0] >= 240 && octets[0] < 256)
    {
        printf("Class of IP address : E (reserved for future use)\n");
    }
    else
    {
        printf("Invalid IP address!");
    }
}