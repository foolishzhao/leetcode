from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n, mIndex = len(nums), 0
        dp, prev = [1] * n, [-1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[mIndex]:
                mIndex = i

        res = []
        while mIndex != -1:
            res.append(nums[mIndex])
            mIndex = prev[mIndex]
        return res[::-1]
