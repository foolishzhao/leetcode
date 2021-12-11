class Solution:
    def permute(self, nums):
        def dfs(nums, curRes):
            if not nums:
                res.append(curRes)
                # return # backtracking
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], curRes + [nums[i]])

        res = []
        dfs(nums, [])
        return res

