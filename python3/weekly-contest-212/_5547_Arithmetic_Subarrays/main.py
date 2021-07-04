from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(subarr):
            for k in range(2, len(subarr)):
                if subarr[k] - subarr[k - 1] != subarr[1] - subarr[0]:
                    return False
            return True

        return [check(sorted(nums[i: j + 1])) for i, j in zip(l, r)]
