from typing import List
import collections
import heapq


class Solution:
    # bellman ford
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(K + 1):
            copy = dist[:]
            for s, d, p in flights:
                copy[d] = min(copy[d], dist[s] + p)
            dist = copy

        return -1 if dist[dst] == float('inf') else dist[dst]

    # dijkstra
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])

        pq, seen = [(0, src, k + 1)], dict()
        while pq:
            d, u, s = heapq.heappop(pq)
            if u == dst:
                return d

            if u in seen and seen[u] >= s:
                continue
            seen[u] = s

            if s:
                for v, w in graph[u]:
                    heapq.heappush(pq, (d + w, v, s - 1))
        return -1


if __name__ == '__main__':
    Solution().findCheapestPrice2(
        4,
        [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
        0,
        3,
        1,
    )
