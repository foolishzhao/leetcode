from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        # <= diff
        def countPair(diff):
            res, i = 0, 0
            for j in range(1, n):
                while nums[j] - nums[i] > diff:
                    i += 1
                res += j - i
            return res

        n = len(nums)
        lo = min([y - x for x, y in zip(nums[:-1], nums[1:])])
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if countPair(mi) < k:
                lo = mi + 1
            else:
                hi = mi
        return lo
