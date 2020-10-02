from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            self.parent[fx] = fy
        else:
            self.parent[fy] = fx
            if self.rank[fx] == self.rank[fy]:
                self.rank[fy] += 1

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def getMST(skip, first):
            uf, mst, ue = UnionFind(n), 0, 0
            if first != -1:
                uf.union(edges[first][0], edges[first][1])
                mst += edges[first][2]
                ue += 1

            for index, edge in sortedEdges:
                if index == skip:
                    continue

                if uf.union(edge[0], edge[1]):
                    mst += edge[2]
                    ue += 1
                    if ue == n - 1:
                        break

            return mst if ue == n - 1 else float('inf')

        sortedEdges = sorted(list(enumerate(edges)), key=lambda x: x[1][2])
        mst = getMST(-1, -1)
        c, pc = list(), list()
        for index, edge in sortedEdges:
            if getMST(index, -1) > mst:
                c.append(index)
            elif getMST(-1, index) == mst:
                pc.append(index)
        return [c, pc]
