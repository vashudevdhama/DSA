import heapq


def dijkstra(graph, sVertex):
    # Initially put dist for each vertex in graph as infinity.
    dist = {v: float('inf') for v in graph}
    # Set the starting vertex distance to zero.
    dist[sVertex] = 0
    # Initialize the priority queue with starting vertex having distance zero.
    p_queue = [(0, sVertex)]
    while len(p_queue):  # While there's some element in p_queue.
        # Get the current distance and vertex using heappop.
        curr_distance, curr_vertex = heapq.heappop(p_queue)

        # Check if no repetition occur, repetion will be there if current distance to neighbour is greater than the respective value in dist list.
        if curr_distance > dist[curr_vertex]:
            continue

        # Find the neighbour which has min distance and push into p_queue.
        for neighbour, edge_wt in graph[curr_vertex].items():
            distance = curr_distance + edge_wt

            # Check if the new path is optimised than the earlier ones.
            if distance < dist[neighbour]:
                # Update the dist for neighbour.
                dist[neighbour] = distance
                # push into p_queue to consider the neighbour for next iteration.
                heapq.heappush(p_queue, (distance, neighbour))
    return dist


graph = {
    'A': {'B': 2, 'C': 5, 'D': 1},
    'B': {'A': 2, 'D': 2, 'C': 3},
    'C': {'B': 3, 'A': 5, 'D': 3, 'Y': 1, 'Z': 5},
    'D': {'A': 1, 'B': 2, 'C': 3, 'Y': 1},
    'E': {'D': 1, 'C': 1, 'Z': 1},
    'F': {'C': 5, 'Y': 1},
}
print(dijkstra(graph, 'D'))
