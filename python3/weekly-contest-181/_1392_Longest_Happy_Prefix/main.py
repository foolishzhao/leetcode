from typing import List


class Solution:
    def longestPrefix(self, s: str) -> str:
        return s[:self.getNext(s)[-1]]

    # nxt[i] = j denotes s[0,..,j-1] == s[i - j,..,i-1]
    def getNext(self, s: str) -> List[int]:
        i, j, n = 0, 1, len(s)
        res = [0] * (n + 1)
        while j < n:
            if s[i] == s[j]:
                i += 1
                j += 1
                res[j] = i
            elif i > 0:
                i = res[i]
            else:
                j += 1

        return res
