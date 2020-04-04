from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        ss = s.split()
        sLen = len(ss)
        wLen = max([len(w) for w in ss])

        res = []
        for i in range(wLen):
            curRes = ""
            for j in range(sLen):
                if len(ss[j]) >= i + 1:
                    curRes += ss[j][i]
                else:
                    curRes += " "
            res.append(curRes.rstrip())

        return res
