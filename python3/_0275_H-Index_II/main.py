from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if citations[mid] >= n - mid:
                if mid == left or citations[mid - 1] < n - mid + 1:
                    return n - mid
                right = mid - 1
            else:
                left = mid + 1

        return 0
