from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licenseCnt = [0] * 26
        for c in licensePlate.lower():
            if c.isalpha():
                licenseCnt[ord(c) - ord('a')] += 1

        res = None
        for word in words:
            if res and len(res) <= len(word):
                continue

            wordCnt = [0] * 26
            for c in word:
                wordCnt[ord(c) - ord('a')] += 1

            hit = True
            for lc, wc in zip(licenseCnt, wordCnt):
                if lc > wc:
                    hit = False
                    break

            if hit and (not res or len(res) > len(word)):
                res = word
        return res
