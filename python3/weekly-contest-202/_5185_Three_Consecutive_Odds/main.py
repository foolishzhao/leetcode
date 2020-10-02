from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n, i = len(arr), 2
        while i < n:
            if arr[i] % 2 == 1 and arr[i - 1] % 2 == 1 and arr[i - 2] % 2 == 1:
                return True
            i += 1
        return False
