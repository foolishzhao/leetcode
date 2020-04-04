import random
from typing import List


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(10):
            w = random.choice(wordlist)
            m = master.guess(w)
            if m == 6:
                return

            wordlist = [w2 for w2 in wordlist if self.matchCount(w, w2) == m]

    def matchCount(self, w1, w2):
        return sum(1 if x == y else 0 for x, y in zip(w1, w2))

    def findSecretWord2(self, wordlist: List[str], master: 'Master') -> None:
        for _ in range(10):
            count = [[0] * 26 for _ in range(6)]
            for w in wordlist:
                for i, c in enumerate(w):
                    count[i][ord(c) - ord('a')] += 1

            # find the max score word
            score, word = 0, ""
            for w in wordlist:
                curScore = 0
                for i, c in enumerate(w):
                    curScore += count[i][ord(c) - ord('a')]
                if curScore > score:
                    score = curScore
                    word = w

            m = master.guess(word)
            if m == 6:
                return

            wordlist = [w for w in wordlist if self.matchCount(w, word) == m]
