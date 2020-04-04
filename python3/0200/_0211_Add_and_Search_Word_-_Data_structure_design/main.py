class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isLeaf = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = TrieNode()
            cur = cur.child[idx]
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchHelper(self.root, word)

    def searchHelper(self, cur: TrieNode, word: str) -> bool:
        if not word:
            return cur.isLeaf

        c = word[0]
        if c == '.':
            for i in range(26):
                if cur.child[i]:
                    if self.searchHelper(cur.child[i], word[1:]):
                        return True
            return False
        else:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                return False
            return self.searchHelper(cur.child[idx], word[1:])
