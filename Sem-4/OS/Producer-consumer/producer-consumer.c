#include <stdio.h>
#include <stdlib.h>
#define MAX 10

int mutex = 1, full = 0, empty = MAX, data = 0;
int buffer[MAX];

int wait(int s)
{
    return --s;
}

int signal(int s)
{
    return ++s;
}

void producer()
{
    // decrementing the value of mutex
    mutex = wait(mutex);

    // Increase the number of full slots
    full = signal(full);

    // decrementing the number of slots available
    empty = wait(empty);

    // incrementing data which means that the data is produced.
    data++;
    printf("Producer produces item: %d\n", data);
    buffer[full - 1] = data;

    // incrementing the value of mutex
    mutex = signal(mutex);

    // for unbounded buffer, consume the produced data immediately
    // consumer()
}

// A function that will resemble the consumer's consumption of data
void consumer()
{
    // decrementing the value of mutex
    mutex = wait(mutex);

    // Decrease the number of full slots
    full = wait(full);

    // incrementing the number of slots available
    empty = signal(empty);

    // buffer[full + 1] = -1;
    printf("Consumer consumes item: %d\n", data);
    data--;

    // incrementing the value of mutex
    mutex = signal(mutex);
}

void main()
{
    int n, i, flag = 0;
    printf("\n1. Enter 1 for Producer"
           "\n2. Enter 2 for Consumer"
           "\n3. Enter 3 for current buffer state"
           "\n4. Enter 4 to Exit\n");

    while (1)
    {
        printf("\nEnter your choice: ");
        scanf("%d", &n);

        switch (n)
        {
        case 1:
            if ((mutex == 1) && (empty != 0)) // or full == MAX
            {
                producer();
            }
            else
            {
                printf("The Buffer is full. New data cannot be produced!\n");
            }
            break;

        case 2:
            if ((mutex == 1) && (full != 0)) // or empty == MAX
            {
                consumer();
            }
            else
            {
                printf("The Buffer is empty! No data to consume!\n");
            }
            break;

        case 3:
            printf("Current buffer state: ");
            for (i = 0; i < full; i++)
            {
                printf("%d ", buffer[i]);
            }
            printf("\n");

            break;

        case 4:
            flag = 1;
            printf("Program end...\n");
            break;

        default:
            printf("Enter valid value!\n");
            break;
        }

        if (flag == 1)
        {
            break;
        }
    }
}
