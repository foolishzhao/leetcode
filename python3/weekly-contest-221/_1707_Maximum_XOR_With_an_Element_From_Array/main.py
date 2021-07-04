from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        cur = self.root
        for i in range(31, -1, -1):
            j = (num >> i) & 1
            if j not in cur:
                cur[j] = {}
            cur = cur[j]

    def query(self, num):
        cur, res = self.root, 0
        for i in range(31, -1, -1):
            j = (num >> i) & 1
            if 1 - j in cur:
                cur = cur[1 - j]
                res |= (1 << i)
            else:
                cur = cur[j]
        return res


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(list(set(nums)))
        queries = sorted(list(enumerate(queries)), key=lambda x: x[1][1])

        n, i, res, trie = len(nums), 0, [-1] * len(queries), Trie()
        for j, (x, m) in queries:
            while i < n and nums[i] <= m:
                trie.insert(nums[i])
                i += 1
            if i > 0:
                res[j] = trie.query(x)
        return res
