class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 1000
        self.nums = [LinkNode(-1) for _ in range(self.cap)]

    def add(self, key: int) -> None:
        cur = self.nums[key % self.cap]
        while cur.next and cur.next.val != key:
            cur = cur.next

        if not cur.next:
            cur.next = LinkNode(key)

    def remove(self, key: int) -> None:
        cur = self.nums[key % self.cap]
        while cur.next and cur.next.val != key:
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        cur = self.nums[key % self.cap]
        while cur.next and cur.next.val != key:
            cur = cur.next

        return cur.next


class MyHashSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 1000
        self.nums = [[] for _ in range(self.cap)]

    def add(self, key: int) -> None:
        li = self.nums[key % self.cap]
        if key not in li:
            li.append(key)

    def remove(self, key: int) -> None:
        li = self.nums[key % self.cap]
        if key in li:
            li.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.nums[key % self.cap]
