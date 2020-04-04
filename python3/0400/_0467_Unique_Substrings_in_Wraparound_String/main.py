class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dt = {c: 1 for c in p}
        curLen, n = 1, len(p)
        for i in range(1, n):
            pc, c = p[i - 1], p[i]
            if ord(c) - ord(pc) == 1 or ord(pc) - ord(c) == 25:
                curLen += 1
            else:
                curLen = 1

            dt[c] = max(dt[c], curLen)

        return sum(dt.values())
