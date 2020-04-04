from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x: x[1])

        i, j = 0, len(nums) - 1
        while i < j:
            t = nums[i][1] + nums[j][1]
            if t == target:
                return [nums[i][0], nums[j][0]]
            elif t > target:
                j -= 1
            else:
                i += 1

        return None

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [i, d[target - v]]
            d[v] = i

        return None


if __name__ == '__main__':
    Solution().twoSum([], 0)
