class Solution:
    def numSub(self, s: str) -> int:
        s += '0'
        n, i, j, res = len(s), 0, 0, 0
        while j < n:
            while s[j] == '1':
                j += 1
            res += (j - i) * (j - i + 1) // 2
            j += 1
            i = j
        return res % (10 ** 9 + 7)
