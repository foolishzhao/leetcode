from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        k = (m + n) // 2
        if (m + n) % 2 == 0:
            return (self.findKth(nums1, 0, m, nums2, 0, n, k) +
                    self.findKth(nums1, 0, m, nums2, 0, n, k + 1)) / 2
        else:
            return self.findKth(nums1, 0, m, nums2, 0, n, k + 1)

    def findKth(self, nums1: List[int], s1: int, m: int, nums2: List[int], s2: int, n: int, k: int) -> int:
        if m > n:
            return self.findKth(nums2, s2, n, nums1, s1, m, k)
        elif m == 0:
            return nums2[s2 + k - 1]
        elif k == 1:
            return min(nums1[s1], nums2[s2])
        else:
            p = min(m, k // 2)
            q = k - p
            if nums1[s1 + p - 1] == nums2[s2 + q - 1]:
                return nums1[s1 + p - 1]
            elif nums1[s1 + p - 1] > nums2[s2 + q - 1]:
                return self.findKth(nums1, s1, p, nums2, s2 + q, n - q, p)
            else:
                return self.findKth(nums1, s1 + p, m - p, nums2, s2, q, q)