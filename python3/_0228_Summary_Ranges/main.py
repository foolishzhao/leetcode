from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        # need to be max_int + 2, for max_int + 1 is continuous to max_int
        nums.append((1 << 31) + 1)

        res = []
        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[j - 1] + 1:
                curRes = str(nums[i])
                if j - 1 > i:
                    curRes += "->" + str(nums[j - 1])
                res.append(curRes)
                i = j
            j += 1

        return res
