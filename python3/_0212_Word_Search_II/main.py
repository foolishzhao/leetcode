from typing import List


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isLeaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = TrieNode()
            cur = cur.child[idx]
        cur.isLeaf = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        res = set()
        for i in range(m):
            for j in range(n):
                self.dfs(res, "", board, i, j, set(), trie.root)

        return list(res)

    def dfs(self, res, curRes, board, i, j, visited, trieNode):
        if trieNode.isLeaf:
            res.add(curRes)

        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
            return

        c = board[i][j]
        idx = ord(c) - ord('a')
        if not trieNode.child[idx]:
            return

        visited.add((i, j))
        self.dfs(res, curRes + c, board, i + 1, j, visited, trieNode.child[idx])
        self.dfs(res, curRes + c, board, i - 1, j, visited, trieNode.child[idx])
        self.dfs(res, curRes + c, board, i, j + 1, visited, trieNode.child[idx])
        self.dfs(res, curRes + c, board, i, j - 1, visited, trieNode.child[idx])
        visited.remove((i, j))
