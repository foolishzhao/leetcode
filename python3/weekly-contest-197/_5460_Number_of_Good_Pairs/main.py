from typing import List
import collections


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return sum([cnt * (cnt - 1) // 2 for cnt in counter.values()])
