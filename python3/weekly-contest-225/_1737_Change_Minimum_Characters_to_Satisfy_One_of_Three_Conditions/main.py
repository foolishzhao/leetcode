class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        na, nb = len(a), len(b)
        if not na or not nb:
            return 0

        aCnt, bCnt = [0] * 26, [0] * 26
        for c in a:
            aCnt[ord(c) - ord('a')] += 1
        for c in b:
            bCnt[ord(c) - ord('a')] += 1

        def strictLess(xTotal, xCnt, yTotal, yCnt):
            res = float('inf')
            for i in range(25):
                res = min(res, xTotal - sum(xCnt[:i + 1]) + yTotal - sum(yCnt[i + 1:]))
            return res

        return min(strictLess(na, aCnt, nb, bCnt), strictLess(nb, bCnt, na, aCnt), na - max(aCnt) + nb - max(bCnt))
