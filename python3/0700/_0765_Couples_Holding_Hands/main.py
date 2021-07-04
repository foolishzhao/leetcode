import collections
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        row, graph = [x // 2 for x in row], collections.defaultdict(list)
        n, i, seen = len(row), 0, set()
        while i < n:
            u, v = row[i], row[i + 1]
            if u != v:
                graph[u].append(v)
                graph[v].append(u)
            else:
                seen.add(u)
            i += 2

        def dfs(u):
            sub = list()
            if u not in seen:
                sub.append(u)
                seen.add(u)
                for v in graph[u]:
                    sub.extend(dfs(v))
            return sub

        return sum([len(dfs(u)) - 1 for u in range(n // 2) if u not in seen])
