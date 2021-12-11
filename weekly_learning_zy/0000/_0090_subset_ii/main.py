from typing import List


class Solution:
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, curRes):
            res.append(curRes)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[i+1:], curRes + [nums[i]])

        res = []
        n = len(nums)
        dfs(nums, [])

        return res

if __name__ == '__main__':
    arr = [4,4,4,1,4]
    a = Solution().subsetsWithDup2(sorted(arr))
    print(a)
