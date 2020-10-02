import functools


class Solution:
    # time complexity: O(n * 26 * n * k)
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def dp(curPos, prev, count, leftK):
            if leftK < 0:
                return float('inf')

            if curPos >= n:
                return 0

            if s[curPos] == prev:
                return dp(curPos + 1, prev, count + 1, leftK) + (count in (1, 9, 99))
            else:
                # keep or delete
                return min(dp(curPos + 1, s[curPos], 1, leftK) + 1, dp(curPos + 1, prev, count, leftK - 1))

        n = len(s)
        return dp(0, "", 0, k)
