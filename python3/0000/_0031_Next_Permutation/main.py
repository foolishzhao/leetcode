from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)
        j = n - 1
        while j > 0:
            if nums[j] > nums[j - 1]:
                break
            j -= 1

        if j == 0:
            nums.reverse()
        else:
            i = j + 1
            while i < n and nums[i] > nums[j - 1]:
                i += 1

            nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]

            u, v = j, n - 1
            while u < v:
                nums[u], nums[v] = nums[v], nums[u]
                u += 1
                v -= 1
