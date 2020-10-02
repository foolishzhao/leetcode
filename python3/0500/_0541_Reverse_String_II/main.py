class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, n, i = "", len(s), 0
        while i < n:
            res += s[i: i + k][::-1]
            res += s[i + k: i + 2 * k]
            i += 2 * k
        return res
