import heapq


# time complexity: O(V*log(V))
def dijkstra(graph, s):
    n = len(graph)
    dist = [float('inf')] * n

    visited = set()

    pq = list([(0, s)])
    while pq:
        d, t = heapq.heappop(pq)
        if t in visited:
            continue

        dist[t] = d
        visited.add(t)

        for nt, nd in enumerate(graph[t]):
            if nd != float('inf'):
                heapq.heappush(pq, (d + nd, nt))

    return dist


if __name__ == '__main__':
    inf = float('inf')
    print(dijkstra([
        [0, 5, inf, 10],
        [inf, 0, 3, inf],
        [inf, inf, 0, 1],
        [inf, inf, inf, 0],
    ], 0))
