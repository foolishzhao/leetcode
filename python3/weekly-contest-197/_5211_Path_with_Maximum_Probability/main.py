from typing import List
import heapq
import collections


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for edge, prob in zip(edges, succProb):
            graph[edge[0]].append((edge[1], prob))
            graph[edge[1]].append((edge[0], prob))

        pq, visited = [(-1, start)], set()
        while pq:
            p, cur = heapq.heappop(pq)
            if cur == end:
                return -p

            if cur in visited:
                continue
            visited.add(cur)

            for nxt, prob in graph[cur]:
                heapq.heappush(pq, (p * prob, nxt))

        return 0
