#include <stdio.h>
#include <stdbool.h>

#define V 4

bool isSafe(bool graph[V][V], int color[])
{
    // check for every edge
    for (int i = 0; i < V; i++)
    {
        for (int j = i + 1; j < V; j++)
        {
            if (graph[i][j] && color[j] == color[i])
                return false;
        }
    }

    return true;
}

bool graphColoring(bool graph[V][V], int m, int i, int color[V])
{
    // base case - if current index reached end
    if (i == V)
    {
        if (isSafe(graph, color))
        {
            printf("\nSolution exists, following are the assigned colors: \n");
            printf("Vertices: ");
            for (int i = 0; i < V; i++)
                printf("\t%d", i);
            printf("\n");

            printf("Colours: ");
            for (int i = 0; i < V; i++)
                printf("\t%d", color[i]);
            printf("\n");

            return true;
        }

        return false;
    }

    // Assign each color from 1 to m
    for (int j = 1; j <= m; j++)
    {
        color[i] = j;

        // recursion to cover the rest vertices
        if (graphColoring(graph, m, i + 1, color))
            return true;

        // BACKTRACK - if no solution found for current color
        color[i] = 0;
    }

    return false;
}

void main()
{
    bool graph[V][V] = {{0, 1, 1, 1},
                        {1, 0, 1, 0},
                        {1, 1, 0, 1},
                        {1, 0, 1, 0}};
    int m = 3;

    int color[V];
    for (int i = 0; i < V; i++)
    {
        color[i] = 0;
    }

    if (graphColoring(graph, m, 0, color) == false) // currentIndex -> 0
        printf("Solution does not exist!");
}
