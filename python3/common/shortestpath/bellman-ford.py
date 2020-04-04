# time complexity: O(V*E)
def bellman_ford(graph, s):
    dist = {}
    for node in graph:
        dist[node] = float('inf')
    dist[s] = 0

    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]

    # exist negative loop
    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                return None

    return dist


if __name__ == '__main__':
    print(bellman_ford({
        'a': {'b': -1, 'c': 4},
        'b': {'c': 3, 'd': 2, 'e': 2},
        'c': {},
        'd': {'b': 1, 'c': 5},
        'e': {'d': -3}
    }, 'a'))
