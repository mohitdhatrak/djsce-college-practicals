#include <stdio.h>
#include <limits.h>

#define V 5

void main()
{
    // int graph[V][V] = {{0, 9, 75, 0, 0},
    //                    {9, 0, 95, 19, 42},
    //                    {75, 95, 0, 51, 66},
    //                    {0, 19, 51, 0, 31},
    //                    {0, 42, 66, 31, 0}};
    int graph[V][V] = {{0, 2, 0, 6, 0},
                       {2, 0, 3, 8, 5},
                       {0, 3, 0, 0, 7},
                       {6, 8, 0, 0, 9},
                       {0, 5, 7, 9, 0}};

    int edges = 0;
    int selectedEdge[V];
    int i, j, x, y;

    for (i = 0; i < V; i++)
    {
        selectedEdge[i] = 0;
    }

    selectedEdge[0] = 1; // selected vertex 0, can take user input

    printf("Edge \t Weight\n");

    while (edges < V - 1)
    {
        int min = INT_MAX;
        x = y = 0;

        for (i = 0; i < V; i++)
        {
            if (selectedEdge[i])
            {
                for (j = 0; j < V; j++)
                {
                    if (!selectedEdge[j] && graph[i][j])
                    {
                        if (min > graph[i][j])
                        {
                            min = graph[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }

        printf("%d - %d \t %d\n", x, y, graph[x][y]);
        selectedEdge[y] = 1;
        edges++;
    }
}