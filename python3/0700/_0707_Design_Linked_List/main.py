class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        prev = self.head
        while index and prev.next != self.tail:
            index -= 1
            prev = prev.next

        return -1 if prev.next == self.tail else prev.next.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAfter(self.head, Node(val))

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAfter(self.tail.prev, Node(val))

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev = self.head
        while prev.next != self.tail and index:
            prev = prev.next
            index -= 1

        if not index:
            self.addAfter(prev, Node(val))

    def addAfter(self, prev, cur):
        cur.next = prev.next
        prev.next.prev = cur

        prev.next = cur
        cur.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev = self.head
        while prev.next != self.tail and index:
            prev = prev.next
            index -= 1

        if prev.next != self.tail:
            prev.next.next.prev = prev
            prev.next = prev.next.next
