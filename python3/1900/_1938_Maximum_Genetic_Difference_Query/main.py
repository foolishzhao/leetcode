from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.val = 0
        self.child = [None] * 2


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        cur = self.root
        for i in range(18, -1, -1):
            idx = (num >> i) & 1
            if not cur.child[idx]:
                cur.child[idx] = TrieNode()
            cur = cur.child[idx]
            cur.val += 1

    def delete(self, num):
        cur = self.root
        for i in range(18, -1, -1):
            idx = (num >> i) & 1
            cur.child[idx].val -= 1
            if not cur.child[idx].val:
                cur.child[idx] = None
                break

            cur = cur.child[idx]

    def maxXor(self, num):
        res, cur = 0, self.root
        for i in range(18, -1, -1):
            if not cur:
                break

            idx = (num >> i) & 1
            if cur.child[1 - idx]:
                res |= 1 << i
                cur = cur.child[1 - idx]
            else:
                cur = cur.child[idx]
        return res


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        child = collections.defaultdict(list)
        for i, par in enumerate(parents):
            child[par].append(i)

        n, trie = len(queries), Trie()
        res, nodeQueries = [0] * n, collections.defaultdict(list)
        for i, (node, val) in enumerate(queries):
            nodeQueries[node].append((i, val))

        def dfs(x):
            if x != -1:
                trie.insert(x)

            for i, val in nodeQueries[x]:
                res[i] = trie.maxXor(val)

            for y in child[x]:
                dfs(y)

            if x != -1:
                trie.delete(x)

        dfs(-1)

        return res
