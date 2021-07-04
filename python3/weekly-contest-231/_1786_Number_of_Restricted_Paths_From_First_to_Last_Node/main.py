import functools
import heapq
import collections
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist, pq = [float('inf')] * (n + 1), [(0, n)]
        while pq:
            w, u = heapq.heappop(pq)
            if dist[u] != float('inf'):
                continue

            dist[u] = w
            for v, w_delta in graph[u]:
                heapq.heappush(pq, (w + w_delta, v))

        @functools.lru_cache(None)
        def dfs(x):
            return 1 if x == n else sum([dfs(y) for y, _ in graph[x] if dist[y] < dist[x]])

        return dfs(1) % (10 ** 9 + 7)
