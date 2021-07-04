from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, q, n = list(), [(0, [0])], len(graph)
        while q:
            u, path = q.pop()
            if u == n - 1:
                res.append(path)
                continue

            for v in graph[u]:
                q.append((v, path + [v]))
        return res

    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        res, n = list(), len(graph)

        def dfs(u, path):
            if u == n - 1:
                res.append(path)
                return

            for v in graph[u]:
                dfs(v, path + [v])

        dfs(0, [0])
        return res
