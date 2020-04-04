class Node:
    def __init__(self):
        self.child = [None] * 26
        self.isLeaf = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = Node()

            cur = cur.child[idx]
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                return False
            cur = cur.child[idx]

        return cur.isLeaf

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                return False
            cur = cur.child[idx]

        return True
