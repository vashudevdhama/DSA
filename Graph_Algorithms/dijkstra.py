'''
With Dijkstra, we find the optimal path with lowest cost.
Time complexity: O(V+Elog(V))
Approach: We start with a source and keep on finding a neighbour node x such that 
the path from source node to node x is the shortest path. 
Once we got such node x, we check all the outgoing edges of x
to see whether there is a better path from s to some unknown vertex through x, until we reach the target node.
'''

import heapq


def dijkstra(graph, sVertex):
    '''
    :param graph: Adjacency list representation of graph.
    :param sVertex: Starting vertex.
    '''
    # Initially put distance as infinity and parent as None for each vertex in graph.
    dist = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    # Set the starting vertex distance to zero.
    dist[sVertex] = 0
    # Initialize the priority queue with starting vertex having distance zero.
    p_queue = [(0, sVertex)]
    while len(p_queue):  # While there's some element in p_queue.
        # Get the current distance and vertex using heappop from p_queue.
        curr_distance, curr_vertex = heapq.heappop(p_queue)

        # Check if no repetition occur, repetion will be there if current distance to neighbour is greater
        # than the respective value stored in dist list.
        if curr_distance > dist[curr_vertex]:
            continue

        # Find the neighbour which has min distance and push into p_queue.
        for neighbour, edge_wt in graph[curr_vertex].items():
            distance = curr_distance + edge_wt

            # Check if the new path is optimised than the earlier ones.
            if distance < dist[neighbour]:
                # Update the dist and parent list for neighbour.
                dist[neighbour] = distance
                parent[neighbour] = curr_vertex
                # push into p_queue to consider the neighbour for next iteration.
                heapq.heappush(p_queue, (distance, neighbour))
    print(dist)
    print(parent)
