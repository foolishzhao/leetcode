from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def helper(nums):
            res, n, i, j = 0, len(nums), 0, 0
            while i < n:
                while j < n and nums[j] < left:
                    j += 1

                if j == n:
                    break

                res += (n - j) * (j - i + 1)
                i = j + 1
                j += 1

            return res

        nums.append(right + 1)
        res, i = 0, 0
        for j, num in enumerate(nums):
            if num > right:
                res += helper(nums[i: j])
                i = j + 1
        return res

    def numSubarrayBoundedMax2(self, nums: List[int], left: int, right: int) -> int:
        j, cnt, res = 0, 0, 0
        for i, num in enumerate(nums):
            if num > right:
                cnt = 0
                j = i + 1
            elif num < left:
                res += cnt
            else:
                cnt = i - j + 1
                res += cnt
        return res
