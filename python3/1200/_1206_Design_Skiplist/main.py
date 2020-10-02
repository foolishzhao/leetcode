import random


class Node:
    def __init__(self, lv, val):
        self.lvs = [None] * lv
        self.val = val


class Skiplist:

    def __init__(self):
        self.maxLevel = 12
        self.head = Node(self.maxLevel, -1)

    def _iter(self, num):
        cur = self.head
        for lv in range(self.maxLevel - 1, -1, -1):
            while cur.lvs[lv] and cur.lvs[lv].val < num:
                cur = cur.lvs[lv]
            yield cur, lv

    def search(self, target: int) -> bool:
        for cur, lv in self._iter(target):
            if cur.lvs[lv] and cur.lvs[lv].val == target:
                return True
        return False

    def add(self, num: int) -> None:
        lv = 1
        while random.random() < 0.5 and lv < self.maxLevel:
            lv += 1
        node = Node(lv, num)

        for cur, curLv in self._iter(num):
            if curLv < lv:
                node.lvs[curLv] = cur.lvs[curLv]
                cur.lvs[curLv] = node

    def erase(self, num: int) -> bool:
        res = False
        for cur, lv in self._iter(num):
            if cur.lvs[lv] and cur.lvs[lv].val == num:
                cur.lvs[lv] = cur.lvs[lv].lvs[lv]
                res = True
        return res
