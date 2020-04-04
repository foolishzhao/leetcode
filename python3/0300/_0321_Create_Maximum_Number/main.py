from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = []
        for i in range(k + 1):
            j = k - i
            if i > m or j > n:
                continue
            res = max(res, self.mergeHelper(self.maxNumberHelper(nums1, i), self.maxNumberHelper(nums2, j)))

        return res

    # can compare list directly
    # max can work on list of list
    def mergeHelper(self, nums1, nums2):
        res = []
        while nums1 or nums2:
            if nums1 > nums2:
                res.append(nums1[0])
                nums1 = nums1[1:]
            else:
                res.append(nums2[0])
                nums2 = nums2[1:]

        return res

    def maxNumberHelper(self, nums, k) -> List[int]:
        n = len(nums)

        st = []
        for i, num in enumerate(nums):
            while st and num > st[-1] and len(st) + n - i > k:
                st.pop()

            if len(st) < k:
                st.append(num)

        return st
