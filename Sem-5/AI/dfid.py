from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def findTarget(self, src, target, max_depth):
        print(src, end=" ")

        if src == target:
            return True
        if max_depth <= 0:
            return False

        for i in self.graph[src]:
            # performs dfs till the max_depth is reached for current findTarget call
            if self.findTarget(i, target, max_depth - 1):
                return True
        return False

    def dfid(self, src, target, max_depth):
        print(f"Input graph: {dict(self.graph)}")

        for i in range(max_depth + 1):
            print(f"\nDepth level {i}: ")
            print("Nodes visited:", end=" ")
            # calls findTarget, for every depth level it starts from root node again
            if self.findTarget(src, target, i):
                return True
            print()  # to add new line

        return False


# Create a graph
#        0           -- depth 0
#      /   \
#     1      2       -- depth 1
#    / \     | \
#   3   4   5   6    -- depth 2

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

src = 0
target = 5

# max_depth = 1
max_depth = 2

print(f"Source node: {src}")
print(f"Target node: {target}")
print(f"Max depth: {max_depth}")

if g.dfid(src, target, max_depth):
    print(
        f"\n\nTarget {target} is reachable from source within max depth of {max_depth}"
    )
else:
    print(
        f"\n\nTarget {target} is NOT reachable from source within max depth of {max_depth}"
    )
