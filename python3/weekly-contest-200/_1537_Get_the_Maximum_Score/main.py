from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        dup = sorted(list(set(nums1).intersection(set(nums2))))
        if not dup:
            return max(sum(nums1), sum(nums2))

        res = 0
        for elem in dup:
            idx1 = nums1.index(elem)
            idx2 = nums2.index(elem)
            res += max(sum(nums1[:idx1 + 1]), sum(nums2[:idx2 + 1]))
            nums1 = nums1[idx1 + 1:]
            nums2 = nums2[idx2 + 1:]
        res += max(sum(nums1), sum(nums2))
        return res % (10 ** 9 + 7)

    def maxSum2(self, nums1: List[int], nums2: List[int]) -> int:
        m, n, i, j = len(nums1), len(nums2), 0, 0
        res, s1, s2 = 0, 0, 0
        while i < m or j < n:
            if i < m and (j == n or nums1[i] < nums2[j]):
                s1 += nums1[i]
                i += 1
            elif j < n and (i == m or nums1[i] > nums2[j]):
                s2 += nums2[j]
                j += 1
            else:
                res += max(s1, s2) + nums1[i]
                i += 1
                j += 1
                s1, s2 = 0, 0
        return (res + max(s1, s2)) % (10 ** 9 + 7)