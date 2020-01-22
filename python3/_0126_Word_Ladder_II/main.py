import string
from queue import Queue
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList:
            return []

        wSet = set(wordList)
        if endWord not in wSet:
            return []

        q = Queue()
        q.put(beginWord)

        ladder = []
        while not q.empty():
            curLadder = []

            sz = q.qsize()
            for i in range(sz):
                w = q.get()
                curLadder.append(w)
                if w == endWord:
                    res = []
                    self.findLaddersHelper(res, [w], ladder, len(ladder) - 1)
                    return res

                for j in range(len(w)):
                    t = w[j]
                    for c in string.ascii_lowercase:
                        if c == t:
                            continue
                        w = w[:j] + c + w[j + 1:]
                        if w in wSet:
                            wSet.remove(w)
                            q.put(w)
                    w = w[:j] + t + w[j + 1:]

            ladder.append(curLadder)

        return []

    def findLaddersHelper(self, res: List[List[str]], oneRes: List[str], ladder: List[List[str]], pos: int):
        if pos < 0:
            cp = oneRes.copy()
            cp.reverse()
            res.append(cp)
            return

        u = oneRes[-1]
        for v in ladder[pos]:
            diff = 0
            for i, j in zip(u, v):
                if i != j:
                    diff += 1

            if diff == 1:
                oneRes.append(v)
                self.findLaddersHelper(res, oneRes, ladder, pos - 1)
                oneRes.pop()


if __name__ == '__main__':
    print(Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
