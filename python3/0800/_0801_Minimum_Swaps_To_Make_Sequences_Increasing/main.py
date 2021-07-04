from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        not_swap, swap = [n] * n, [n] * n
        not_swap[0], swap[0] = 0, 1

        for i in range(1, n):
            # 1st check
            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                not_swap[i] = not_swap[i - 1]
                swap[i] = swap[i - 1] + 1

            # 2nd check, could satisfy two checks at the same time
            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                not_swap[i] = min(not_swap[i], swap[i - 1])
                swap[i] = min(swap[i], not_swap[i - 1] + 1)

        return min(not_swap[-1], swap[-1])
