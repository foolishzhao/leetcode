class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.arr = [0] * k
        self.front = k - 1
        self.rear = 0
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.cnt += 1
        self.arr[self.front] = value
        self.front = (self.front - 1) % self.k
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.cnt += 1
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.cnt -= 1
        self.front = (self.front + 1) % self.k
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.cnt -= 1
        self.rear = (self.rear - 1) % self.k
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.front + 1) % self.k]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cnt == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cnt == self.k


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, node):
        self.insert(self.head, node)

    def insertLast(self, node):
        self.insert(self.tail.prev, node)

    def insert(self, prev, cur):
        cur.next = prev.next
        cur.prev = prev
        prev.next.prev = cur
        prev.next = cur

    def deleteFront(self):
        self.delete(self.head.next)

    def deleteLast(self):
        self.delete(self.tail.prev)

    def delete(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = node.next = None

    def getFront(self):
        return self.head.next.val

    def getLast(self):
        return self.tail.prev.val


class MyCircularDeque2:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.cnt = 0
        self.dlist = DList()

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.cnt += 1
        self.dlist.insertFront(Node(value))
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.cnt += 1
        self.dlist.insertLast(Node(value))
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.cnt -= 1
        self.dlist.deleteFront()
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.cnt -= 1
        self.dlist.deleteLast()
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.dlist.getFront()

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.dlist.getLast()

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cnt == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cnt == self.k
