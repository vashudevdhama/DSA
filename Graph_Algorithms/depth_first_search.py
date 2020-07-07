'''
In DFS, we recursively explore graph.
Time complexity: O(V+E)
Approach: First we explore the choices of starting vertex s and then recursively explores all outgoing edges of vertex s.
'''


def DFS(adj, V):
    '''
    :param adj: Adjacency list represntation of the graph.
    :param V: List of all the vertices of the graph.
    '''
    parent = {}
    # Explore the choices of startign vertex by traversing list of vertices.
    for s in V:
        # check if s is not already traversed.
        if s not in parent:
            # assign the parent to start node.
            parent[s] = None
            # call the recursive function to explore the various outgoing paths of start vertex s.
            DFS_visit(adj, s, parent)

    print(parent)


def DFS_visit(adj, s, parent):
    '''
    :param adj: Adjacency list represntation of the graph.
    :param s: Current vertex.
    '''
    # Explore all the neighbours of current vertex s.
    for v in adj[s]:
        # check if v is not already traversed.
        if v not in parent:
            # assign the parent.
            parent[v] = s
            # Recursively call itself to explore furthur deepen paths with v as current node.
            DFS_visit(adj, v)
