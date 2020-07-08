'''
Graph representation in Adjacency list form.
Note: Here linked list is used to store the neighbours.
'''


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Graph:
    adj = {}

    def addEdge(self, s, d):
        '''
        :param s: source node.
        :param d: destination node.
        '''
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

# Example graph:
# (2) <-- (1)*    (5) --> (7)
#  |       |    /  |    /  |
#  v       v  /    v  /    v
# (4)     (3) --> (6) --> (8)

# Adjacency representation of above example graph:
# 1:  -> 2 -> 3
# 2:  -> 4
# 3:  -> 5 -> 6
# 5:  -> 6 -> 7
# 6:  -> 7 -> 8
# 7:  -> 8


'''Uncomment following lines to test the code.'''

# V = [1, 2, 3, 4, 5, 6, 7, 8]
# E = [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6),
#      (5, 6), (5, 7), (6, 7), (6, 8), (7, 8)]

# graph = Graph()

# for s, d in E:
#     graph.addEdge(s, d)

# graph.printGraph()
