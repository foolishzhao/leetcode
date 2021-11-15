from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res, i, n = 0, 0, len(arr)
        while i < n - 2:
            if arr[i] >= arr[i + 1]:
                i += 1
                continue

            j = i + 1
            while j < n and arr[j] > arr[j - 1]:
                j += 1

            if j == n:
                break

            if arr[j] == arr[j - 1]:
                i = j
                continue

            while j < n and arr[j] < arr[j - 1]:
                j += 1

            res = max(res, j - i)
            i = j - 1

        return res
