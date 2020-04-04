from queue import Queue
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        level = 0
        q = Queue()
        q.put(beginWord)

        while not q.empty():
            sz = q.qsize()
            level += 1

            for i in range(sz):
                word = q.get()
                for j in range(len(word)):
                    t = word[j]
                    for c in string.ascii_lowercase:
                        if c == t:
                            continue
                        word = word[:j] + c + word[j + 1:]
                        if word in wordSet:
                            if word == endWord:
                                return level + 1
                            q.put(word)
                            wordSet.remove(word)
                    word = word[:j] + t + word[j + 1:]

        return 0
