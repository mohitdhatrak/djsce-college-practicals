#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

#define V 5

int minKey(int key[], bool vertexStatus[])
{
    int min = INT_MAX, minIndex;

    for (int v = 0; v < V; v++)
    {
        if (vertexStatus[v] == false && key[v] < min)
        {
            min = key[v];
            minIndex = v;
        }
    }

    return minIndex;
}

void prims(int graph[V][V], int src)
{
    int parent[V];
    int key[V];
    bool vertexStatus[V];

    for (int i = 0; i < V; i++)
    {
        key[i] = INT_MAX;
        vertexStatus[i] = false;
    }

    // make src vertex 0 so that this vertex is picked as first vertex
    key[src] = 0;

    // First node is always root of MST
    parent[src] = -1;

    for (int count = 0; count < V - 1; count++)
    {
        int u = minKey(key, vertexStatus);

        vertexStatus[u] = true;

        // update key value and parent index of adjacent vertices
        for (int v = 0; v < V; v++)
        {
            if (!vertexStatus[v] && graph[u][v] && graph[u][v] < key[v])
            {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    printf("Edge \t Weight\n");
    for (int i = 1; i < V; i++)
    {
        printf("%d - %d \t %d \n", parent[i], i, graph[parent[i]][i]);
    }
}

void main()
{
    int graph[V][V] = {{0, 2, 0, 6, 0},
                       {2, 0, 3, 8, 5},
                       {0, 3, 0, 0, 7},
                       {6, 8, 0, 0, 9},
                       {0, 5, 7, 9, 0}};

    prims(graph, 0);
}
