from typing import List
import collections


class Solution:
    def count(self, nums1, nums2):
        c = collections.defaultdict(int)
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                c[nums2[i] * nums2[j]] += 1

        return sum(c[n1 ** 2] for n1 in nums1)

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.count(nums1, nums2) + self.count(nums2, nums1)
