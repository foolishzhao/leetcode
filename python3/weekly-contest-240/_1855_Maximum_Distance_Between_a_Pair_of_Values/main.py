from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res, i, j = 0, 0, 0
        while i < len(nums1):
            while j < len(nums2) and nums2[j] >= nums1[i]:
                j += 1
            res = max(res, j - i - 1)
            i += 1
        return res