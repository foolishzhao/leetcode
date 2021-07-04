from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(u):
            for v in graph[u]:
                if not mark[v]:
                    mark[v] = 1 - mark[u]
                    if not dfs(v):
                        return False
                elif mark[v] == mark[u]:
                    return False
            return True

        n, mark = len(graph), [None] * len(graph)
        for i in range(n):
            if not mark[i]:
                mark[i] = 0
                if not dfs(i):
                    return False
        return True

    def isBipartite2(self, graph: List[List[int]]) -> bool:
        def bfs(u):
            q = [u]
            while q:
                u = q.pop()
                for v in graph[u]:
                    if not mark[v]:
                        mark[v] = 1 - mark[u]
                        q.append(v)
                    elif mark[v] == mark[u]:
                        return False
            return True

        n, mark = len(graph), [None] * len(graph)
        for i in range(n):
            if not mark[i]:
                mark[i] = 0
                if not bfs(i):
                    return False
        return True
