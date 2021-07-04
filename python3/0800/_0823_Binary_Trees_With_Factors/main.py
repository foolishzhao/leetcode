from typing import List
import collections


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n, st, arr = len(arr), set(arr), sorted(arr)
        dt = collections.defaultdict(int)

        for i in range(n):
            dt[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in st:
                    dt[arr[i]] += dt[arr[j]] * dt[arr[i] // arr[j]]

        return sum(dt.values()) % (10 ** 9 + 7)
