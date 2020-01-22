from typing import List


class BinaryIndexTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = [0] * (self.n + 1)
        for i, v in enumerate(arr):
            self.update(i, v)

    def update(self, i: int, delta: int):
        i += 1
        while i <= self.n:
            self.arr[i] ^= delta
            i += i & -i

    def queryPrefix(self, i: int) -> int:
        i += 1
        res = 0
        while i:
            res ^= self.arr[i]
            i -= i & -i

        return res

    def queryRange(self, i: int, j: int) -> int:
        return self.queryPrefix(j) ^ self.queryPrefix(i - 1)


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        bit = BinaryIndexTree(arr)
        return [bit.queryRange(pair[0], pair[1]) for pair in queries]
