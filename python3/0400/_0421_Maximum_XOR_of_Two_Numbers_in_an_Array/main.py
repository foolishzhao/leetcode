from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(31)[::-1]:
            res <<= 1
            prefixes = {x >> i for x in nums}
            for prefix in prefixes:
                if ((res | 1) ^ prefix) in prefixes:
                    res |= 1
                    break

        return res


class TrieNode:
    def __init__(self):
        self.child = [None] * 2


class Solution2:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = TrieNode()
        for num in nums:
            cur = trie
            for i in range(32)[::-1]:
                idx = (num >> i) & 1
                if not cur.child[idx]:
                    cur.child[idx] = TrieNode()
                cur = cur.child[idx]

        res = 0
        for num in nums:
            cur, curRes = trie, 0
            for i in range(32)[::-1]:
                idx = (num >> i) & 1
                if cur.child[1 - idx]:
                    curRes += 1 << i
                    cur = cur.child[1 - idx]
                else:
                    # in this case, every non-leaf node must have at least one child
                    cur = cur.child[idx]
            res = max(res, curRes)

        return res
