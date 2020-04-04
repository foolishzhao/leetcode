from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        res, n = [], len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                u, v = j + 1, n - 1
                while u < v:
                    t = nums[i] + nums[j] + nums[u] + nums[v]
                    if t == target:
                        res.append([nums[i], nums[j], nums[u], nums[v]])
                        u += 1
                        while u < v and nums[u] == nums[u - 1]:
                            u += 1
                    elif t > target:
                        v -= 1
                    else:
                        u += 1

        return res
