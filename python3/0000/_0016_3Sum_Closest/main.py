from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) >= 3:
            nums.sort()

            res, n = sum(nums[:3]), len(nums)
            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                j, k = i + 1, n - 1
                while j < k:
                    t = nums[i] + nums[j] + nums[k]
                    if abs(t - target) < abs(res - target):
                        res = t

                    if t == target:
                        return t
                    elif t > target:
                        k -= 1
                    else:
                        j += 1

            return res

        return 0
