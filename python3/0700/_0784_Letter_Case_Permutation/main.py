from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        curSt = {''}
        for c in s:
            tmpSt = {c.lower(), c.upper()}
            curSt = {cur + x for cur in curSt for x in tmpSt}
        return list(curSt)
