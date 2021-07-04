from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        lo, hi = 0, len(letters) - 1
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if letters[mi] <= target:
                lo = mi + 1
            else:
                hi = mi
        return letters[lo]
