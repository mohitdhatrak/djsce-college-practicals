#include <stdio.h>

struct item
{
    int num;
    float p, w, ratio; // profit, weight, p/w ratio
};

void bubbleSort(struct item arr[], int n)
{
    int i, j;
    struct item temp;

    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j].ratio < arr[j + 1].ratio)
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void greedyKnapsack(int n, float capacity, struct item items[])
{
    float maxProfit = 0.0;
    float weightIncluded[n];

    for (int i = 0; i < n; i++)
    {
        weightIncluded[i] = 0;
    }

    bubbleSort(items, n);

    for (int i = 0; capacity > 0; i++)
    {
        if (capacity >= items[i].w)
        {
            capacity -= items[i].w;
            weightIncluded[i] = items[i].w;
            maxProfit += items[i].p;
        }
        else
        {
            weightIncluded[i] = capacity;
            maxProfit += (capacity / items[i].w) * items[i].p;
            capacity = 0.0;
        }
    }

    printf("\nMax profit: %0.4f\n", maxProfit);
    printf("Weight included per item: \n");
    for (int i = 0; i < n; i++)
    {
        printf("For item %d, weight included: %0.2f\n", items[i].num, weightIncluded[i]);
    }
}

void main()
{
    int n, i;
    float capacity;

    printf("Enter number of items: ");
    scanf("%d", &n);

    printf("Enter max capacity: ");
    scanf("%f", &capacity);

    struct item items[n];

    printf("Enter profits and weights of all items:\n");
    for (i = 0; i < n; i++)
    {
        printf("Enter profit and weight of item %d: ", i + 1);
        scanf("%f %f", &items[i].p, &items[i].w);
        items[i].ratio = items[i].p / items[i].w;
        items[i].num = i + 1;
    }

    greedyKnapsack(n, capacity, items);
}