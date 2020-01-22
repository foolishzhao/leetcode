import random

"""
    reference: http://cs-cjl.com/2019/05_08_skiplist_principle_and_impl
    ->                     5             ->               None  
    -> 1        ->         5        ->         9    ->    None    
    -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
"""


class Node:
    def __init__(self, level: int, key: int, val: int):
        self.key = key
        self.val = val
        self.forward = [None] * level


class SkipList:
    def __init__(self, maxLevel: int, p: float):
        self.maxLevel = maxLevel
        self.p = p
        self.level = 0
        self.head = Node(maxLevel, 0, 0)

    def get(self, key: int) -> int:
        cur = self.head
        for level in range(self.level - 1, -1, -1):
            while cur.forward[level] and cur.forward[level].key < key:
                cur = cur.forward[level]

        cur = cur.forward[0]
        return cur.val if cur and cur.key == key else None

    def put(self, key: int, val: int) -> None:
        prev = [None] * self.maxLevel
        cur = self.head
        for level in range(self.level - 1, -1, -1):
            while cur.forward[level] and cur.forward[level].key < key:
                cur = cur.forward[level]
            prev[level] = cur

        cur = cur.forward[0]
        if cur and cur.key == key:
            cur.val = val
        else:
            newLevel = self.getLevel()
            if newLevel > self.level:
                for level in range(self.level, newLevel):
                    prev[level] = self.head
                self.level = newLevel

            node = Node(newLevel, key, val)
            for level in range(newLevel):
                node.forward[level] = prev[level].forward[level]
                prev[level].forward[level] = node

    def remove(self, key: int) -> int:
        prev = [None] * self.maxLevel
        cur = self.head
        for level in range(self.level - 1, -1, -1):
            while cur.forward[level] and cur.forward[level].key < key:
                cur = cur.forward[level]
            prev[level] = cur

        cur = cur.forward[0]
        if cur and cur.key == key:
            val = cur.val

            for level in range(self.level):
                if prev[level].forward[level] != cur:
                    break

                prev[level].forward[level] = cur.forward[level]

            while self.level and not self.head.forward[self.level - 1]:
                self.level -= 1

            return val
        else:
            return None

    def getLevel(self):
        level = 1
        for i in range(1, self.maxLevel):
            if random.random() < self.p:
                level += 1

        return level

    def __repr__(self):
        valList = []
        cur = self.head.forward[0]
        while cur:
            valList.append(str(cur.key))
            cur = cur.forward[0]

        return "->".join(valList)


if __name__ == '__main__':
    sl = SkipList(5, 0.25)
    for i in range(10):
        sl.put(i + 1, i + 1)

    print(sl)
    print(sl.get(2))
    print(sl.get(3))
    print(sl.get(4))
    print(sl.get(7))
    print(sl.get(11))

    print(sl.remove(3))
    print(sl.get(3))
