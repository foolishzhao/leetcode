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
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edges = collections.defaultdict(dict)
        for u, v, w in flights:
            edges[u][v] = w

        pq = [(0, src, K + 1)]
        while pq:
            p, u, k = heapq.heappop(pq)
            if u == dst:
                return p

            if k > 0:
                for v, w in edges[u].items():
                    heapq.heappush(pq, (p + w, v, k - 1))

        return -1


if __name__ == '__main__':
    Solution().findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1)
