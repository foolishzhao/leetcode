from typing import List


class Solution:
    # only one decode way
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n, i = len(bits), 0
        while i < n - 1:
            i += 2 if bits[i] else 1
        return i == n - 1
