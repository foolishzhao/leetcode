from typing import List


class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.child = [None] * 26
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = TrieNode()
            cur = cur.child[idx]
        cur.isLeaf = True
        cur.word = word

    def search(self):
        res, md = "", 0
        for c in self.root.child:
            if c and c.isLeaf:
                cw, cd = self._search(c, 1)
                if cd > md or (cd == md and cw < res):
                    res, md = cw, cd
        return res

    def _search(self, cur, depth):
        res, md = cur.word, depth
        for c in cur.child:
            if c and c.isLeaf:
                cw, cd = self._search(c, depth + 1)
                if cw:
                    if cd > md or (cd == md and cw < res):
                        res, md = cw, cd
        return res, md


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.search()

    def longestWord2(self, words: List[str]) -> str:
        words.sort()

        st, res = {""}, ""
        for w in words:
            if w[:-1] in st:
                st.add(w)
                if len(w) > len(res):
                    res = w
        return res
