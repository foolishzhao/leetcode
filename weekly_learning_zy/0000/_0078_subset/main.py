from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(curRes, pos):
            if pos == n:
                res.append(curRes)
                return

            dfs(curRes, pos + 1)
            dfs(curRes + [nums[pos]], pos + 1)

        res, n = list(), len(nums)
        dfs(list(), 0)
        return res


class Solution:
    def subset(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, curRes):
            res.append(curRes)
            for i in range(len(nums)):
                dfs(nums[i + 1:], curRes + [nums[i]])

        res = []
        n = len(nums)
        dfs(sorted(nums), [])

        return res

if __name__ == '__main__':
    arr = [1,2,3]
    a = Solution().subsets(sorted(arr))
    print(a)