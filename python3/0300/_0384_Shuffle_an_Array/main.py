from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.index = list(range(len(nums)))

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        i = 0
        while i < len(self.nums):
            while self.index[i] != i:
                nIdx = self.index[i]
                self.nums[i], self.nums[nIdx] = self.nums[nIdx], self.nums[i]
                self.index[i], self.index[nIdx] = self.index[nIdx], self.index[i]
            i += 1

        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)
        while n:
            idx = random.randint(0, n - 1)
            self.nums[idx], self.nums[n - 1] = self.nums[n - 1], self.nums[idx]
            self.index[idx], self.index[n - 1] = self.index[n - 1], self.index[idx]
            n -= 1
        return self.nums


if __name__ == '__main__':
    obj = Solution([1, 2, 3])
    obj.shuffle()
    obj.reset()
    obj.shuffle()
