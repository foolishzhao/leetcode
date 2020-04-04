from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dt = dict()
        for c in "qwertyuiop":
            dt[c] = 1
        for c in "asdfghjkl":
            dt[c] = 2
        for c in "zxcvbnm":
            dt[c] = 3

        res = list()
        for w in words:
            st = set()
            for c in w:
                st.add(dt[c.lower()])
            if len(st) == 1:
                res.append(w)
        return res
