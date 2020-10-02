from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        n = len(words)
        res = list()
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
