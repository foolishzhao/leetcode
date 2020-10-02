class Node:
    def __init__(self):
        self.child = [None] * 128
        self.val = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key, val):
        cur = self.root
        for c in key:
            if not cur.child[ord(c)]:
                cur.child[ord(c)] = Node()
            cur = cur.child[ord(c)]
        cur.val = val

    def sumPrefix(self, prefix):
        cur = self.root
        for c in prefix:
            if not cur.child[ord(c)]:
                return 0
            cur = cur.child[ord(c)]
        return self.sumPrefixHelper(cur)

    def sumPrefixHelper(self, cur):
        if not cur:
            return 0

        res = cur.val
        for c in cur.child:
            res += self.sumPrefixHelper(c)
        return res


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.sumPrefix(prefix)


class MapSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dt = dict()

    def insert(self, key: str, val: int) -> None:
        self.dt[key] = val

    def sum(self, prefix: str) -> int:
        return sum([v for k, v in self.dt.items() if k.startswith(prefix)])
