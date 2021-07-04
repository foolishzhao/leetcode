from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res, i = list(), 0
        for j, c in enumerate(s + '$'):
            if c != s[i]:
                if j - i >= 3:
                    res.append([i, j - 1])
                i = j

        return res
