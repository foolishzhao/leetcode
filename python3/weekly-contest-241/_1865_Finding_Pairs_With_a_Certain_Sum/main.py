from typing import List
import collections


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.dt = collections.defaultdict(int)
        for x in nums2:
            self.dt[x] += 1

    def add(self, index: int, val: int) -> None:
        x = self.nums2[index]
        self.nums2[index] += val
        self.dt[x] -= 1
        self.dt[x + val] += 1

    def count(self, tot: int) -> int:
        res = 0
        for x in self.nums1:
            res += self.dt[tot - x]
        return res
