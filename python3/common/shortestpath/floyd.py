def floyd(graph):
    n = len(graph)

    # k denotes maximum-index middle nodes among the shortest path from i to j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


if __name__ == '__main__':
    inf = float('inf')
    print(floyd([
        [0, 5, inf, 10],
        [inf, 0, 3, inf],
        [inf, inf, 0, 1],
        [inf, inf, inf, 0],
    ]))
