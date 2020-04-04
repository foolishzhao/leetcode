from typing import List
import collections
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.index = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.index[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index[target])


class Solution2:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        return random.choice([i for i, num in enumerate(self.nums) if num == target])


class Solution3:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res, count = -1, 0
        for i, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, count) == 0:
                    res = i
                count += 1
        return res
