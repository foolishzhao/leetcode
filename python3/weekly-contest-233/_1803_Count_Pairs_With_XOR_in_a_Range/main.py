from typing import List


class TrieNode:
    def __init__(self):
        self.val = 0
        self.child = [None] * 2


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, x):
        cur = self.root
        for i in reversed(range(15)):
            b = (x >> i) & 1
            if not cur.child[b]:
                cur.child[b] = TrieNode()
            cur = cur.child[b]
            cur.val += 1

    def count(self, x, high):
        cur, res = self.root, 0
        for i in reversed(range(15)):
            if not cur:
                break

            b = (x >> i) & 1
            h = (high >> i) & 1
            if h:
                res += cur.child[b].val if cur.child[b] else 0
                cur = cur.child[1 - b]
            else:
                cur = cur.child[b]
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie, res = Trie(), 0
        for num in nums:
            res += trie.count(num, high + 1) - trie.count(num, low)
            trie.insert(num)
        return res
