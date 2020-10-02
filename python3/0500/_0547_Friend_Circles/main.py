from typing import List
import collections


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        edges = collections.defaultdict(list)
        n, res = len(M), 0
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1 and i != j:
                    edges[i].append(j)
                    edges[j].append(i)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                res += 1
                self.dfs(edges, i, visited)
        return res

    def dfs(self, edges, i, visited):
        visited[i] = True
        for nx in edges[i]:
            if not visited[nx]:
                self.dfs(edges, nx, visited)

    def findCircleNum2(self, M: List[List[int]]) -> int:
        def dfs(x):
            visited[x] = True
            for y in range(n):
                if M[x][y] == 1 and not visited[y]:
                    dfs(y)

        res, n = 0, len(M)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [0] * n
        self.rank = [0] * n
        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return

        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1

        print(x, y, self.find(x), self.find(y))


class Solution2:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    uf.union(i, j)

        # let uf's parent points to root
        for i in range(n):
            uf.find(i)

        return len(set(uf.parent))


if __name__ == '__main__':
    Solution2().findCircleNum([
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1]],
    )
