class Solution:
    def modifyString(self, s: str) -> str:
        chs, n = list(s), len(s)
        for i, c in enumerate(chs):
            if c == '?':
                for j in range(26):
                    nc = chr(ord('a') + j)
                    if (i == 0 or nc != chs[i - 1]) and (i == n - 1 or nc != chs[i + 1]):
                        chs[i] = nc
                        break
        return ''.join(chs)

    def modifyString2(self, s: str) -> str:
        chs, n = list(s), len(s)
        for i, c in enumerate(chs):
            if c == '?':
                for nc in 'abc':
                    if (i == 0 or nc != chs[i - 1]) and (i == n - 1 or nc != chs[i + 1]):
                        chs[i] = nc
                        break
        return ''.join(chs)
