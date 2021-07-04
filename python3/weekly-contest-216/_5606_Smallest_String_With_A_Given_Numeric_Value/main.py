class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res, i, k = ['a'] * n, n - 1, k - n
        while k:
            t = min(k, 25)
            res[i] = chr(ord('a') + t)
            k -= t
            i -= 1
        return ''.join(res)
