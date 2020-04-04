import collections


class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = Node(0, 0, 0)
        self.tail = Node(0, 0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.n = 0

    def append(self, node):
        node.next = self.head.next
        self.head.next.prev = node

        node.prev = self.head
        self.head.next = node

        self.n += 1

    def pop(self, node):
        if not node:
            node = self.tail.prev

        node.next.prev = node.prev
        node.prev.next = node.next

        self.n -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.sz = 0
        self.keyDict = dict()
        self.freqDict = collections.defaultdict(DLinkedList)
        self.minFreq = 0

    def _update(self, node):
        freq = node.freq
        self.freqDict[freq].pop(node)
        if self.freqDict[freq].n == 0 and self.minFreq == freq:
            self.minFreq += 1

        node.freq += 1
        freq = node.freq
        self.freqDict[freq].append(node)

    def get(self, key: int) -> int:
        if key in self.keyDict:
            node = self.keyDict[key]
            self._update(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.keyDict:
            node = self.keyDict[key]
            node.val = value
            self._update(node)
        else:
            if self.sz == self.cap:
                oldNode = self.freqDict[self.minFreq].pop(None)
                self.keyDict.pop(oldNode.key)
                self.sz -= 1
            node = Node(key, value, 1)
            self.keyDict[key] = node
            self.freqDict[1].append(node)
            self.sz += 1
            self.minFreq = 1
