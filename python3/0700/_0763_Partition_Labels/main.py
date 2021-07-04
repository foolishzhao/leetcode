from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        def getIndex(x):
            return ord(x) - ord('a')

        end = [-1] * 26
        for i, c in enumerate(S):
            end[getIndex(c)] = i

        res, i, n = list(), 0, len(S)
        while i < n:
            u, v = i, end[getIndex(S[i])]
            while u < v:
                v = max(v, end[getIndex(S[u])])
                u += 1

            res.append(v - i + 1)
            i = v + 1
        return res
