from typing import List
import collections


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        inDegree, graph = [0] * n, collections.defaultdict(list)
        for x, y in richer:
            inDegree[y] += 1
            graph[x].append(y)

        rich, seen = collections.defaultdict(set), set()
        for _ in range(n):
            for x in range(n):
                if inDegree[x] == 0 and x not in seen:
                    seen.add(x)
                    rich[x].add(x)

                    for y in graph[x]:
                        rich[y] |= rich[x]
                        inDegree[y] -= 1

        res = list()
        for x in range(n):
            r = None
            for y in rich[x]:
                if r is None or quiet[y] < quiet[r]:
                    r = y
            res.append(r)
        return res

    def loudAndRich2(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = collections.defaultdict(list)
        for x, y in richer:
            graph[y].append(x)

        def dfs(x):
            if res[x] >= 0:
                return res[x]

            res[x] = x
            for y in graph[x]:
                if quiet[res[x]] > quiet[dfs(y)]:
                    res[x] = res[y]
            return res[x]

        res = [-1] * n
        for i in range(n):
            dfs(i)
        return res
