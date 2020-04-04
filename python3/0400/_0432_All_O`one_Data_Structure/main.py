class Node:
    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None

    def addKey(self, key):
        self.keys.add(key)

    def removeKey(self, key):
        self.keys.remove(key)


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyCount = dict()

        self.countHead = Node()
        self.countTail = Node()
        self.countHead.next = self.countTail
        self.countTail.prev = self.countHead

        self.countToNode = dict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keyCount:
            self.keyCount[key] += 1
        else:
            self.keyCount[key] = 1

        cnt = self.keyCount[key]
        if cnt not in self.countToNode:
            self.countToNode[cnt] = Node()
            curNode = self.countToNode[cnt]
            if cnt > 1:
                prevNode = self.countToNode[cnt - 1]
            else:
                prevNode = self.countHead

            curNode.next = prevNode.next
            curNode.prev = prevNode
            prevNode.next.prev = curNode
            prevNode.next = curNode

        self.countToNode[cnt].addKey(key)
        if cnt > 1:
            self.countToNode[cnt - 1].removeKey(key)
            if not self.countToNode[cnt - 1].keys:
                self.countToNode[cnt - 1].prev.next = self.countToNode[cnt - 1].next
                self.countToNode[cnt - 1].next.prev = self.countToNode[cnt - 1].prev
                del self.countToNode[cnt - 1]

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keyCount:
            cnt = self.keyCount[key]
            if cnt == 1:
                del self.keyCount[key]
            else:
                self.keyCount[key] -= 1
                if cnt - 1 not in self.countToNode:
                    self.countToNode[cnt - 1] = Node()
                    curNode = self.countToNode[cnt - 1]

                    nextNode = self.countToNode[cnt]

                    curNode.next = nextNode
                    curNode.prev = nextNode.prev
                    nextNode.prev.next = curNode
                    nextNode.prev = curNode

            self.countToNode[cnt - 1].addKey(key)
            self.countToNode[cnt].removeKey(key)
            if not self.countToNode[cnt].keys:
                self.countToNode[cnt].next.prev = self.countToNode[cnt].prev
                self.countToNode[cnt].prev.next = self.countToNode[cnt].next
                del self.countToNode[cnt]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.countTail.prev.keys:
            key = self.countTail.prev.keys.pop()
            self.countTail.prev.keys.add(key)
            return key
        else:
            return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.countHead.next.keys:
            key = self.countHead.next.keys.pop()
            self.countHead.next.keys.add(key)
            return key
        else:
            return ""
