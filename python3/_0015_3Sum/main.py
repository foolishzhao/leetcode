from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()

        n = len(nums)
        if n >= 3:
            nums.sort()

            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                j, k = i + 1, n - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        j += 1

        return res
