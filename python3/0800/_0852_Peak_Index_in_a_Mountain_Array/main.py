from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return i

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while hi - lo >= 1:
            mi = (lo + hi) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi

        return lo if arr[lo] > arr[hi] else hi
