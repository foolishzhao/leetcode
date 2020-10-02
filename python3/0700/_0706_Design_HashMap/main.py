class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 1000
        self.store = [[] for _ in range(self.cap)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        li = self.store[key % self.cap]
        for i in range(len(li)):
            if li[i][0] == key:
                li[i][1] = value
                return
        li.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        li = self.store[key % self.cap]
        for i in range(len(li)):
            if li[i][0] == key:
                return li[i][1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        li = self.store[key % self.cap]
        for i in range(len(li)):
            if li[i][0] == key:
                li.pop(i)
                return
