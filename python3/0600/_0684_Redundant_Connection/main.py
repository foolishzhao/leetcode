from typing import List
import collections


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
        return True


class Solution:
    # time complexity: O(n)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        index = {tuple(edge): i for i, edge in enumerate(edges)}

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(p, x):
            if visited[x] == -1:
                return [x]

            visited[x] = -1
            for y in graph[x]:
                if y != p:
                    res = dfs(x, y)
                    if res:
                        return [x] + res
            visited[x] = 1
            return None

        n = len(edges)
        visited = [0] * (n + 1)
        for i in range(1, n + 1):
            if not visited[i]:
                chain = dfs(0, i)
                if chain:
                    res, lc = -1, len(chain)
                    for j in range(lc - 2, -1, -1):
                        if chain[j] == chain[-1]:
                            return edges[res]
                        a, b = chain[j], chain[j + 1]
                        res = max(res, index[(min(a, b), max(a, b))])

    # time complexity: O(n^2)
    # have one and only one circle
    # build adj progressively, for edge (u, v), if use built adj, u can come to v, then the circle found
    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        def dfs(u, v, p):
            if u == v:
                return True

            for nxt in adj[u]:
                if nxt != p:
                    if dfs(nxt, v, u):
                        return True
            return False

        adj = collections.defaultdict(list)
        for fr, to in edges:
            if dfs(fr, to, 0):
                return [fr, to]

            adj[fr].append(to)
            adj[to].append(fr)

    # time complexity: O(n*log(n))
    def findRedundantConnection3(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
