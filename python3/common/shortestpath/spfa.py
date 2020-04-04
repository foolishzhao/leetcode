# time complexity: O(k*E)， k is all vertexes average enqueue times
def spfa(graph, s):
    dist = {}
    for node in graph:
        dist[node] = float('inf')
    dist[s] = 0

    q = list([s])
    while q:
        sz = len(q)
        for i in range(sz):
            u = q[i]
            for v in graph[u]:
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]
                    q.append(v)
        q = q[sz:]

    # exist negative loop
    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                return None

    return dist


if __name__ == '__main__':
    print(spfa({
        'a': {'b': -1, 'c': 4},
        'b': {'c': 3, 'd': 2, 'e': 2},
        'c': {},
        'd': {'b': 1, 'c': 5},
        'e': {'d': -3}
    }, 'a'))
