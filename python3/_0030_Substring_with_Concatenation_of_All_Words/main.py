from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        wLen, wsLen, sLen = len(words[0]), len(words), len(s)
        wDict = dict()
        for w in words:
            wDict[w] = wDict.get(w, 0) + 1

        res = []
        for i in range(sLen - wLen * wsLen + 1):
            if self.dfs(s[i: i + wLen * wsLen], wDict, wLen):
                res.append(i)

        return res

    def dfs(self, s: str, dt: dict, wLen: int) -> bool:
        if not s:
            return True

        w = s[:wLen]
        if dt.get(w, 0) > 0:
            dt[w] -= 1
            res = self.dfs(s[wLen:], dt, wLen)
            dt[w] += 1

            if res:
                return True

        return False

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        wLen, wsLen, sLen = len(words[0]), len(words), len(s)
        wDict = dict()
        for w in words:
            wDict[w] = wDict.get(w, 0) + 1

        res = []
        for i in range(sLen - wLen * wsLen + 1):
            j = i
            dt = wDict.copy()
            while j < i + wLen * wsLen:
                w = s[j: j + wLen]
                if dt.get(w, 0) > 0:
                    dt[w] -= 1
                    j += wLen
                else:
                    break

            if j == i + wLen * wsLen:
                res.append(i)

        return res
