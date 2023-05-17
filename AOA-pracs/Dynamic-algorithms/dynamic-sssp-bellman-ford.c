#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// E is the total no. of edges in graph
int bellmanFord(int graph[20][20], int V, int E, int edge[20][2])
{
    int i, u, v, k, distance[20], parent[20], s, flag = 1;

    for (i = 0; i < V; i++)
    {
        distance[i] = INT_MAX;
        parent[i] = -1;
    }

    printf("Enter source: ");
    scanf("%d", &s);

    distance[s] = 0;

    for (i = 0; i < V - 1; i++)
    {
        for (k = 0; k < E; k++)
        {
            u = edge[k][0];
            v = edge[k][1];

            if (distance[u] + graph[u][v] < distance[v])
            {
                distance[v] = distance[u] + graph[u][v];
                parent[v] = u;
            }
        }
    }

    for (k = 0; k < E; k++)
    {
        u = edge[k][0];
        v = edge[k][1];
        if (distance[u] + graph[u][v] < distance[v])
            flag = 0;
    }

    if (flag)
    {
        for (i = 0; i < V; i++)
        {
            printf("Vertex %d -> cost = %d\n", i + 1, distance[i]);
        }
    }

    return flag;
}

void main()
{
    int V, edge[20][2], graph[20][20], i, j, k = 0;

    printf("Enter no. of vertices: ");
    scanf("%d", &V);

    printf("Enter graph in matrix form: \n");
    for (i = 0; i < V; i++)
        for (j = 0; j < V; j++)
        {
            printf("graph[%d][%d]: ", i, j);
            scanf("%d", &graph[i][j]);

            if (graph[i][j] != 0)
            {
                edge[k][0] = i;
                edge[k][1] = j;
                k++;
            }
        }

    // graph[][] = {{0, -1, 4, 0, 0},
    //              {0, 0, 3, 2, 2},
    //              {0, 0, 0, 0, 0},
    //              {0, 1, 5, 0, 0},
    //              {0, 0, 0, -3, 0}};

    if (bellmanFord(graph, V, k, edge)) // k passed is no. of edges -> E
        printf("\nNo negative weight cycle!\n");
    else
        printf("\nNegative weight cycle exists!\n");
}