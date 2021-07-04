from typing import List
import collections


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def isSubtree(nodes):
            if len(nodes) < 2:
                return False

            q = [nodes.pop()]
            while q:
                u, deleted = q.pop(0), set()
                for v in nodes:
                    if v in graph[u]:
                        q.append(v)
                        deleted.add(v)

                for x in deleted:
                    nodes.remove(x)
            return not nodes

        def dist(nodes):
            def dfs(u, p):
                d = 0
                for v in graph[u]:
                    if v != p and v in nodes:
                        d = max(d, dfs(v, u) + 1)
                return d

            return max([dfs(u, -1) for u in nodes])

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)

        res = [0] * (n - 1)
        for i in range(1 << n):
            nodes = set(j for j in range(n) if i & (1 << j))
            if isSubtree(nodes.copy()):
                res[dist(nodes) - 1] += 1
        return res
