from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        firstVal, firstCnt = 0, 0
        secondVal, secondCnt = 0, 0
        for num in nums:
            if num == firstVal:
                firstCnt += 1
            elif num == secondVal:
                secondCnt += 1
            elif not firstCnt:
                firstVal = num
                firstCnt = 1
            elif not secondCnt:
                secondVal = num
                secondCnt = 1
            else:
                firstCnt -= 1
                secondCnt -= 1

        # corner case: [0, 0, 0]
        return [x for x in {firstVal, secondVal} if nums.count(x) > len(nums) // 3]
