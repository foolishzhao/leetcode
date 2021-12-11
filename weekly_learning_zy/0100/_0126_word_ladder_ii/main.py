import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]: 
        wordSet = set(wordList)
        if endWord not in wordSet:
            return list()
        
        layer, seen = {beginWord: [[beginWord]]}, {beginWord}
        while layer:
            nextLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                
                for i, c in enumerate(word):
                    for j in range(26):
                        nc = chr(ord('a') + j)
                        if nc != c:
                            nWord = word[:i] + nc + word[i + 1:]
                            if nWord in wordSet and nWord not in seen:
                                nextLayer[nWord] += [x + [nWord] for x in layer[word]]
            layer = nextLayer
            for word in layer:
                seen.add(word)
            
        return list()
