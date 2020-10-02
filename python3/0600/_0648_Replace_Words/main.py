from typing import List


class Node:
    def __init__(self):
        self.isLeaf = False
        self.child = [None] * 26


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for w in word:
            if not cur.child[ord(w) - ord('a')]:
                cur.child[ord(w) - ord('a')] = Node()
            cur = cur.child[ord(w) - ord('a')]
        cur.isLeaf = True

    def search(self, word):
        cur = self.root
        for i, w in enumerate(word):
            if not cur.child[ord(w) - ord('a')]:
                return None
            cur = cur.child[ord(w) - ord('a')]
            if cur.isLeaf:
                return word[:i + 1]
        return None


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for w in dict:
            trie.insert(w)

        n, j, res = len(sentence), 0, ""
        while j < n:
            while j < n and sentence[j].isspace():
                res += sentence[j]
                j += 1

            i = j
            while j < n and not sentence[j].isspace():
                j += 1
            w = trie.search(sentence[i: j])
            res += w if w else sentence[i: j]

        return res
