import collections


class Solution:
    def maxProduct(self, s: str) -> int:
        def palindromeLen(mask):
            i, j, l = 0, n - 1, 0
            while i <= j:
                if (1 << i) & mask == 0:
                    i += 1
                elif (1 << j) & mask == 0:
                    j -= 1
                elif s[i] != s[j]:
                    return 0
                else:
                    l += 2 if i != j else 1
                    i += 1
                    j -= 1
            return l

        n, mask, dt = len(s), (1 << len(s)) - 1, collections.defaultdict(int)
        for i in range(1, mask + 1):
            dt[i] = palindromeLen(i)

        res = 0
        for i in range(mask, 0, -1):
            if dt[i] * (n - dt[i]) > res:
                j = i ^ mask
                while j > 0:
                    res = max(res, dt[i] * dt[j])
                    j = (j - 1) & (i ^ mask)
        return res
