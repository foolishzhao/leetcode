from typing import List


class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.word = None
        self.child = [None] * 128


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        cur = self.root
        for c in s:
            if not cur.child[ord(c)]:
                cur.child[ord(c)] = TrieNode()
            cur = cur.child[ord(c)]
        cur.isLeaf = True
        cur.word = s

    def search(self, prefix):
        cur = self.root
        for c in prefix:
            if not cur.child[ord(c)]:
                return list()
            cur = cur.child[ord(c)]

        return self._helper(cur)

    def _helper(self, cur):
        res = list()
        if not cur:
            return res

        if cur.isLeaf:
            res.append(cur.word)

        for c in cur.child:
            res.extend(self._helper(c))

        return res


class Solution:
    # Time Limit Exceeded
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = list()
        if len(words) < 2:
            return res

        dt = {w: i for i, w in enumerate(words)}

        trie = Trie()
        for w in words:
            trie.insert(w)

        for w in words:
            for c in trie.search(self.getShortestPalindromePrefix(w)):
                if c != w and self.isPalindrome(c + w):
                    res.append([dt[c], dt[w]])

        return res

    def getShortestPalindromePrefix(self, s):
        t = s + "#" + s[::-1]
        nxt = self.getNext(t)
        return s[nxt[-1]:][::-1]

    def getNext(self, s: str) -> List[int]:
        n = len(s)
        nxt = [0] * (n + 1)

        i, j = 1, 0
        while i < n:
            if s[i] == s[j]:
                i += 1
                j += 1
                nxt[i] = j
            elif j > 0:
                j = nxt[j]
            else:
                i += 1

        return nxt

    def palindromePairs2(self, words: List[str]) -> List[List[int]]:
        dt = {w: i for i, w in enumerate(words)}

        res = list()
        for i, w in enumerate(words):
            n = len(w)
            for cut in range(n + 1):
                if self.isPalindrome(w[cut:]):
                    if w[:cut][::-1] in dt:
                        j = dt[w[:cut][::-1]]
                        if j != i:
                            res.append([i, j])
                if cut and self.isPalindrome(w[:cut]):
                    if w[cut:][::-1] in dt:
                        j = dt[w[cut:][::-1]]
                        if j != i:
                            res.append([j, i])

        return res

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
