#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

#define V 9
// #define V 6

int minDistance(int dist[], bool processedVertices[])
{
    int minIndex;
    int min = INT_MAX;

    for (int v = 0; v < V; v++)
    {
        if (processedVertices[v] == false && dist[v] <= min)
        {
            min = dist[v];
            minIndex = v;
        }
    }

    return minIndex;
}

void dijkstra(int graph[V][V], int src)
{
    int dist[V]; // holds the shortest distance from src to i th vertex

    bool processedVertices[V]; // marks vertices - true means vertex processed

    // initialize all distances as infinite and processedVertices as false
    for (int i = 0; i < V; i++)
    {
        dist[i] = INT_MAX;
        processedVertices[i] = false;
    }

    // distance of source vertex from itself is always 0
    dist[src] = 0;

    for (int count = 0; count < V - 1; count++)
    {
        int u = minDistance(dist, processedVertices);

        // mark the picked vertex as processed
        processedVertices[u] = true;

        // update dist value of the adjacent vertices of the picked vertex.
        for (int v = 0; v < V; v++)

            // update dist[v] only if -
            // 1- v is not in processedVertices
            // 2- there is an edge from u to v
            // 3- dist[u] + graph[u][v] < dist[v]
            if (!processedVertices[v] && graph[u][v] && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }

    printf("Vertex \t Distance from Source\n");
    for (int i = 0; i < V; i++)
    {
        printf("  %d \t\t %d\n", i, dist[i]);
    }
}

void main()
{
    int graph[V][V] = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                       {4, 0, 8, 0, 0, 0, 0, 11, 0},
                       {0, 8, 0, 7, 0, 4, 0, 0, 2},
                       {0, 0, 7, 0, 9, 14, 0, 0, 0},
                       {0, 0, 0, 9, 0, 10, 0, 0, 0},
                       {0, 0, 4, 14, 10, 0, 2, 0, 0},
                       {0, 0, 0, 0, 0, 2, 0, 1, 6},
                       {8, 11, 0, 0, 0, 0, 1, 0, 7},
                       {0, 0, 2, 0, 0, 0, 6, 7, 0}};
    // int graph[V][V] = {{0, 1, 5, 0, 0, 0},
    //                    {0, 0, 2, 2, 1, 0},
    //                    {0, 0, 0, 0, 2, 0},
    //                    {0, 0, 0, 0, 3, 1},
    //                    {0, 0, 0, 0, 0, 2},
    //                    {0, 0, 0, 0, 0, 0}};

    dijkstra(graph, 0);
}
