from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, curRes):
            if not nums:
                res.append(curRes)
            for i in range(len(nums)):
                if i < len(nums) - 1 and nums[i] == nums[i+1]:
                    continue
                dfs(nums[:i]+nums[i+1:],curRes + [nums[i]])
        res = []
        dfs(sorted(nums), [])
        return res
