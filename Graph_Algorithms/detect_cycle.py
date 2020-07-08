'''
Check if there's any cycle present in a graph using DFS.
'''


def detectCycleDFS(graph):
    '''
    :param graph: Adjacency list representation of graph.
    :rtype: boolean
    '''
    parent = {}
    for s in graph.keys():
        if s not in parent:
            parent[s] = None
            if dfs_visit(graph, s, parent):
                return True
    return False


def dfs_visit(graph, s, parent):
    '''
    :param graph: Adjacency list representation of graph.
    :param s: Current vertex in graph.
    :param parent: Parent dictionary for the vertices.
    :rtype: boolean
    '''
    for v in graph[s]:
        if v not in parent:
            parent[v] = s
            if dfs_visit(graph, v, parent):
                return True
        else:
            if parent[s] != v and parent[s] != None:
                print_cycle(s, v, parent)  # print the cycle detected.
                return True
    return False


def print_cycle(s, v, parent):
    '''
    :param s: Current vertex in the graph.
    :param v: Neighbour vertex of current vertex edge between which cause cycle.
    :param parent: Parent dictionary for the vertices.
    '''
    curr = s
    while(curr != v):
        print(curr, end=' ')
        curr = parent[curr]
    print(curr, end=' ')
    print(s)


'''
Uncomment following lines to test the program
'''
# graph_undirected = {
#     3: [2, 4, 1],
#     4: [3, 5],
#     5: [4, 2],
#     1: [2, 6, 3],
#     2: [1, 3, 5],
#     6: [1],
# }
# print("Cycle detected: ", detectCycleDFS(graph_undirected))

# graph_directed = {
#     1: [2, 3],
#     2: [3],
#     3: [],
#     4: [1, 5, 6],
#     5: [6],
#     6: [],
# }
# print("Cycle detected: ", detectCycleDFS(graph_directed))
