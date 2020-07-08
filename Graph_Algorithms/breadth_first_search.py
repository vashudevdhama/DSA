'''
By BFS, we visit all nodes reachable from a given node s.
Time complexity: O(V+E)
Approach: We look at the nodes reachable in 0 moves, 1 moves .... d moves until we ran out of graph.
'''


def bfs(s, graph):
    '''
    :param s: starting vertex for traversal.
    :param graph: adjacency list representation of graph.
    '''
    parent = {s: None}
    current_nodes = [s]  # To store nodes at same level.
    traversal = []  # To store bfs traversal path.

    while current_nodes:
        next_nodes = []  # To store next level nodes.
        # Traverse for every node in current_nodes list.
        for u in current_nodes:
            traversal.append(u)  # Add that to traversal list.
            # Traverse every next level node connected to current node u.
            if u not in graph:  # check if any such node u exist as a key in adjacency list.
                continue
            for v in graph[u]:
                # Check if node already been covered.
                if v not in parent:
                    parent[v] = u
                    next_nodes.append(v)
        # Make next_nodes as current_nodes and loop again.
        current_nodes = next_nodes
    print(traversal)
    print(parent)


# (2) <-- (1)*    (5) --> (7)
#  |       |    /  |    /  |
#  v       v  /    v  /    v
# (4)     (3) --> (6) --> (8)
'''Uncomment below lines to test the code.'''

# graph_undirected = {
#     1: [2, 3],
#     2: [4],
#     3: [5, 6],
#     5: [6, 7],
#     6: [7, 8],
#     7: [8],
# }

# bfs(1, graph_undirected)
