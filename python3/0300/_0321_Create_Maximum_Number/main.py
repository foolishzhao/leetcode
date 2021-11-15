from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def merge(arr1, arr2):
            arr3 = list()
            while arr1 or arr2:
                if arr1 > arr2:
                    arr3.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    arr3.append(arr2[0])
                    arr2 = arr2[1:]
            return arr3

        def helper(arr1, k):
            st = list()
            for i, v in enumerate(arr1):
                while st and st[-1] < v and len(st) + len(arr1) - i - 1 >= k:
                    st.pop()

                if len(st) < k:
                    st.append(v)
            return st

        m, n, res = len(nums1), len(nums2), list()
        for u in range(k + 1):
            v = k - u
            if u > m or v > n:
                continue

            res = max(res, merge(helper(nums1, u), helper(nums2, v)))
        return res
