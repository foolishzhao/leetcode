from typing import List


class UnionFind:
    def __init__(self, n, m):
        self.parent = list(range(n))
        self.group = [0] * n
        self.m = m
        self.m_cnt = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parent[px] = py

        if self.group[px] == self.m:
            self.m_cnt -= 1

        if self.group[py] == self.m:
            self.m_cnt -= 1

        self.group[py] += self.group[px]
        self.group[px] = 0

        if self.group[py] == self.m:
            self.m_cnt += 1

    def set_group(self, x):
        self.group[x] = 1
        if self.m == 1:
            self.m_cnt += 1

    def has(self):
        return self.m_cnt


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res, n = -1, len(arr)
        bits, uf = [0] * n, UnionFind(n, m)
        for i, v in enumerate(arr):
            bits[v - 1] = 1
            uf.set_group(v - 1)
            if v > 1 and bits[v - 2] == 1:
                uf.union(v - 2, v - 1)
            if v < n and bits[v] == 1:
                uf.union(v - 1, v)

            if uf.has():
                res = i + 1
        return res

    def findLatestStep2(self, arr: List[int], m: int) -> int:
        res, n = -1, len(arr)
        # length of group
        length = [0] * (n + 2)
        # count of length
        count = [0] * (n + 1)

        for i, v in enumerate(arr):
            left, right = length[v - 1], length[v + 1]
            length[v] = length[v - left] = length[v + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[v]] += 1
            if count[m]:
                res = i + 1
        return res
