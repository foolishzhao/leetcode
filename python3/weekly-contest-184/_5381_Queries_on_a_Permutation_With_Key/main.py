from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = list()
        P = list(range(1, m + 1))
        for q in queries:
            res.append(P.index(q))
            P.remove(q)
            P.insert(0, q)
        return res


class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)

    def update(self, idx, delta):
        idx += 1
        while idx <= self.n:
            self.arr[idx] += delta
            idx += idx & -idx

    def sumPrefix(self, idx):
        idx += 1
        res = 0
        while idx:
            res += self.arr[idx]
            idx -= idx & -idx
        return res


class Solution2:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        bit = BinaryIndexedTree(2 * m)
        dt = {}
        for i in range(m):
            dt[i + 1] = i + m
            bit.update(i + m, 1)

        res = list()
        for q in queries:
            res.append(bit.sumPrefix(dt[q] - 1))
            bit.update(dt[q], -1)
            dt[q] = m - 1
            bit.update(dt[q], 1)
            m -= 1
        return res
