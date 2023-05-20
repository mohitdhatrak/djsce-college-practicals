#include <stdio.h>
#include <limits.h>
#define N 10
#define INF INT_MAX

void DVR(int n, int source, int graph[N][N])
{
    int distance[N];
    int nextHop[N];

    int i, j, k;
    for (i = 1; i <= n; i++)
    {
        distance[i] = INF;
        nextHop[i] = -1;
    }

    distance[source] = 0;

    for (k = 1; k <= n; k++)
    {
        for (i = 1; i <= n; i++)
        {
            for (j = 1; j <= n; j++)
            {
                if (graph[i][j] != 0 && distance[i] != INF)
                {
                    int newDist = distance[i] + graph[i][j];
                    if (newDist < distance[j])
                    {
                        distance[j] = newDist;
                        nextHop[j] = i;
                    }
                }
            }
        }
    }

    printf("Shortest path from node %d\n", source);
    for (i = 1; i <= n; i++)
    {
        printf("node %d => %d distance = %d, via node = %d\n", source, i, distance[i], nextHop[i]);
    }
}

void main()
{
    int n, graph[N][N], source;
    int i, j;

    printf("Enter number of nodes: ");
    scanf("%d", &n);
    printf("Enter source node: ");
    scanf("%d", &source);
    printf("Enter adjacency graph: \n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            scanf("%d", &graph[i][j]);
        }
    }

    // graph[3][3] = {{0, 2, 7},
    //                {2, 0, 1},
    //                {7, 1, 0}};

    DVR(n, source, graph);
}
