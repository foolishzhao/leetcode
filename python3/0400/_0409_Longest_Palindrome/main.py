import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dt = collections.defaultdict(int)
        for c in s:
            dt[c] += 1

        res, oddExist = 0, False
        for c, cnt in dt.items():
            if cnt % 2 == 0:
                res += cnt
            else:
                res += cnt - 1
                oddExist = True

        return res + 1 if oddExist else res
