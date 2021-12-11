from queue import Queue
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        # {}代表一个set ,()是元组
        q, seen, lv = [beginWord], {beginWord}, 0
        while q:
            lv += 1
            sz = len(q)
            for _ in range(sz):
                word = q.pop(0)
                if word == endWord:
                    return lv

                for i, c in enumerate(word):
                    for j in range(26):
                        nc = chr(ord('a') + j)
                        if nc != c:
                            nWord = word[:i] + nc + word[i + 1:]
                            if nWord in wordSet and nWord not in seen:
                                q.append(nWord)
                                seen.add(nWord)
        return 0
