class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dt = {}

    def get(self, key: int) -> int:
        res = -1
        if key in self.dt:
            cur = self.dt[key]
            res = cur.val
            self.delete(cur)
            self.putToHead(cur)

        return res

    def put(self, key: int, value: int) -> None:
        if key in self.dt:
            cur = self.dt[key]
            # new value might be different from old one
            cur.val = value
            self.delete(cur)
            self.putToHead(cur)
        else:
            cur = Node(key, value)
            self.putToHead(cur)
            self.dt[key] = cur

            if self.size < self.capacity:
                self.size += 1
            else:
                self.dt.pop(self.tail.prev.key)
                self.delete(self.tail.prev)

    def putToHead(self, node: Node) -> None:
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def delete(self, node: None) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
    lru.get(2)
    lru.put(4, 4)
