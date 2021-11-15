from typing import List
from math import sqrt
import collections


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[py] += self.rank[px] == self.rank[py]


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def primeFactors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n = n / 2

            for i in range(3, int(sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n = n / i

            if n > 2:
                factors.add(n)
            return factors

        uf, n = UnionFind(len(nums)), len(nums)
        dt = collections.defaultdict(list)
        for i in range(n):
            primes = primeFactors(nums[i])
            for x in primes:
                dt[x].append(i)

        for vals in dt.values():
            for val in vals[1:]:
                uf.union(vals[0], val)

        newNums = sorted(list(enumerate(nums)), key=lambda x: x[1])
        for newIdx, newNum in enumerate(newNums):
            if uf.find(newIdx) != uf.find(newNum[0]):
                return False
        return True

    def gcdSort2(self, nums: List[int]) -> bool:
        mx = max(nums)
        spf = list(range(mx + 1))  # smallest prime factor
        for i in range(2, int(sqrt(mx)) + 1):
            if spf[i] != i:
                continue

            for j in range(i * i, mx + 1, i):
                if spf[j] == j:
                    spf[j] = i

        uf = UnionFind(mx + 1)
        for i, num in enumerate(nums):
            while num > 1:
                f = spf[num]
                num //= f
                uf.union(f, nums[i])

        for x, y in zip(nums, sorted(nums)):
            if uf.find(x) != uf.find(y):
                return False
        return True
