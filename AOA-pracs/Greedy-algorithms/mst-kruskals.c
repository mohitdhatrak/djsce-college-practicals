#include <stdio.h>
#include <stdlib.h>

#define V 9

struct edge
{
    int u, v, weight;
};

void bubbleSort(struct edge arr[], int n)
{
    int i, j;
    struct edge temp;

    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j].weight > arr[j + 1].weight)
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int noLoopFormed()
{
}

int addEdge(int edgesTracker[V][V], int u, int v)
{
    if (noLoopFormed())
    {
        for (int i = 0; i < V; i++)
        {
            edgesTracker[u][v] = 1;
            edgesTracker[v][u] = 1;
        }

        return 1;
    }

    return 0;
}

void kruskals(int graph[V][V], struct edge selectedEdges[])
{
    int i, j, existingEdges = 0;

    // to count number of unique edges available
    for (i = 0; i < V; i++)
    {
        for (j = 0; j < V; j++)
        {
            if (graph[i][j] != 0)
            {
                existingEdges++;
                graph[j][i] = 0; // to avoid duplicates, as graph is undirected
            }
        }
    }

    struct edge sortedEdges[existingEdges];
    int k = 0;

    // to store data of all available edges
    for (i = 0; i < V; i++)
    {
        for (j = 0; j < V; j++)
        {
            if (graph[i][j] != 0)
            {
                sortedEdges[k].u = i;
                sortedEdges[k].v = j;
                sortedEdges[k].weight = graph[i][j];
                k++;
            }
        }
    }

    bubbleSort(sortedEdges, existingEdges); // sorted edges according to weights

    int edgesTracker[V][V];
    for (i = 0; i < V; i++)
    {
        for (j = 0; j < V; j++)
        {
            edgesTracker[i][j] = 0;
        }
    }

    k = 1; // keep track of how many edges selected, only V - 1 needed
    selectedEdges[0] = sortedEdges[0];
    addEdge(edgesTracker, sortedEdges[0].u, sortedEdges[0].v);

    for (i = 1; i < existingEdges; i++)
    {
        if (k == V - 1)
            break;

        if (addEdge(edgesTracker, sortedEdges[i].u, sortedEdges[i].v))
        {
            selectedEdges[k] = sortedEdges[i];
            k++;
        }
    }
}

void main()
{
    int i, cost = 0;

    int graph[V][V] = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                       {4, 0, 8, 0, 0, 0, 0, 11, 0},
                       {0, 8, 0, 7, 0, 4, 0, 0, 2},
                       {0, 0, 7, 0, 9, 14, 0, 0, 0},
                       {0, 0, 0, 9, 0, 10, 0, 0, 0},
                       {0, 0, 4, 14, 10, 0, 2, 0, 0},
                       {0, 0, 0, 0, 0, 2, 0, 1, 6},
                       {8, 11, 0, 0, 0, 0, 1, 0, 7},
                       {0, 0, 2, 0, 0, 0, 6, 7, 0}};

    struct edge selectedEdges[V - 1];

    printf("\nThe edges of Minimum Cost Spanning Tree are:\n");
    kruskals(graph, selectedEdges);

    for (i = 0; i < V - 1; i++)
    {
        printf("\n%d - %d : %d", selectedEdges[i].u, selectedEdges[i].v, selectedEdges[i].weight);
        cost += selectedEdges[i].weight;
    }
    printf("\nSpanning tree cost: %d", cost);
}
