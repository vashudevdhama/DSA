'''
By BFS, we visit all nodes reachable from a given node s.
Time complexity: O(V+E)
Approach: We look at the nodes reachable in 0 moves, 1 moves .... d moves until we ran out of graph.
'''


def BFS(adj, s):
    level = {s: 0}  # starting node -> level 0.
    parent = {s: None}  # starting node -> parent None.
    i = 1  # to keep track of node's level.
    frontier = [s]  # nodes at level i-1.
    while frontier:
        next = []  # nodes at level i.
        print(frontier)
        for u in frontier:  # for every element in level i-1 nodes list.
            # for every element in adjacency list at index of node with level i-1.
            if u not in adj:  # check if any such node u exist as a key in adjacency list.
                continue
            # To traverse the neighbour nodes, assign the value corresponding to the key from adjacency list
            current = adj[u]
            while current:  # Check if neigbour exists.
                if current.val not in level:  # check if level isn't already assigned.
                    # assign the level i to the element.
                    level[current.val] = i
                    # assign element at level i as a parent to element at level i-1.
                    parent[current.val] = u
                    next.append(current.val)  # udpate level i nodes list.
                current = current.next
        # make the level i nodes list as frontier(i.e., level i-1 nodes list).
        frontier = next
        i += 1  # and update the node's level count.
    # print(level) # print level of each node in graph with respect to 's' starting node.
    # print(parent) # print parent of each node in graph.


'''
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Graph:
    adj = {}

    def addEdge(self, s, d):
        node = Node(d)
        if s not in self.adj:
            self.adj[s] = node
        else:
            current = self.adj[s]
            while (current.next):
                current = current.next
            current.next = node

    def printGraph(self):
        for i in self.adj:
            print("{}: ".format(i), end=' ')
            current = self.adj[i]
            while current:
                print("-> {}".format(current.val), end=' ')
                current = current.next
            print()

# (2) <-- (1)*    (5) --> (7)
#  |       |    /  |    /  |
#  v       v  /    v  /    v
# (4)     (3) --> (6) --> (8)

V = [1, 2, 3, 4, 5, 6, 7, 8]
E = [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6),
     (5, 6), (5, 7), (6, 7), (6, 8), (7, 8)]
graph = Graph()
for s, d in E:
    graph.addEdge(s, d)
graph.printGraph()
BFS(graph.adj, 1)
'''
