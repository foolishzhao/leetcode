from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, cnt = None, 0
        for num in nums:
            if not cnt:
                cur, cnt = num, 1
            elif num == cur:
                cnt += 1
            else:
                cnt -= 1

        return cur
