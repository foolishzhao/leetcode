from typing import List
import collections


class Node:
    def __init__(self):
        self.child = [None] * 26
        self.isLeaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = Node()
            cur = cur.child[idx]
        cur.isLeaf = True

    def search(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                return False
            cur = cur.child[idx]
        return cur.isLeaf


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i, c in enumerate(word):
            for j in range(26):
                rc = chr(ord('a') + j)
                if rc != c and self.trie.search(word[:i] + rc + word[i + 1:]):
                    return True
        return False


class MagicDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dt = collections.defaultdict(list)

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            for i, c in enumerate(word):
                self.dt[word[:i] + word[i + 1:]].append((i, c))

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i, c in enumerate(word):
            for j, cc in self.dt[word[:i] + word[i + 1:]]:
                if i == j and c != cc:
                    return True
        return False
