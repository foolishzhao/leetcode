class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dt = dict()
        for i in range(26):
            dt[chr(ord('A') + i)] = [-1, -1]

        res = 0
        for i, c in enumerate(s):
            k, j = dt[c]
            res += (j - k) * (i - j)
            dt[c] = [j, i]

        for c in dt:
            k, j = dt[c]
            res += (j - k) * (len(s) - j)

        return res % (10 ** 9 + 7)
