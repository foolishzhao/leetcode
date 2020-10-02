import math


class Solution:
    # A * (times + 1) include all patterns of len(B) then A can form, add more times doesn't help
    def repeatedStringMatch(self, A: str, B: str) -> int:
        times = math.ceil(len(B) / len(A))
        if B in (A * times):
            return times
        if B in (A * (times + 1)):
            return times + 1
        return -1
