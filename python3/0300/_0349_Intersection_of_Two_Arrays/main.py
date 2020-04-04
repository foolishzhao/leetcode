from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        if not nums1 or not nums2:
            return res

        nums1.sort()
        nums2.sort()
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                while i + 1 < m and nums1[i + 1] == nums1[i]:
                    i += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res
