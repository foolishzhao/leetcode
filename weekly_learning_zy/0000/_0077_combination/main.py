from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, curRes):
            if len(curRes) == k:
                res.append(curRes)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], curRes + [nums[i]])
        res = []
        nums = list(range(1, n+1))
        dfs(nums, [])
        return res
    def combine2(self, nums: List[int], k: int) -> List[List[int]]:
        def dfs(nums, curRes):
            if len(curRes) == k:
                res.append(curRes)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], curRes + [nums[i]])
        res = []
        dfs(nums, [])
        return res

if __name__ == '__main__':
    # a = Solution().combine(4,3)
    b = [1,8,7,7]
    a = Solution().combine2(sorted(b), 3)
    print(a)
