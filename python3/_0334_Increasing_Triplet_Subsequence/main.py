from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False

        one, two = float('inf'), float('inf')
        for num in nums:
            if num > two:
                return True
            elif num > one:
                two = min(two, num)
            else:
                one = min(one, num)

        return False
