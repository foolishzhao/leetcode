from typing import List
import collections


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, p):
            counter = collections.Counter()
            for v in graph[u]:
                if v != p:
                    counter.update(dfs(v, u))
            counter.update(labels[u])
            res[u] = counter[labels[u]]
            return counter

        res = [0] * n
        dfs(0, -1)
        return res
