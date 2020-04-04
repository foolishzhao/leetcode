import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.index = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        newIndex = len(self.nums)
        self.nums.append(val)
        if val not in self.index:
            self.index[val] = {newIndex}
            return True
        else:
            self.index[val].add(newIndex)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.index:
            oldIndex = self.index[val].pop()
            if not self.index[val]:
                del self.index[val]

            lastIndex, lastVal = len(self.nums) - 1, self.nums[-1]
            self.nums[oldIndex], self.nums[-1] = self.nums[-1], self.nums[oldIndex]

            if lastVal != val or lastIndex != oldIndex:
                self.index[lastVal].remove(lastIndex)
                self.index[lastVal].add(oldIndex)
            self.nums.pop()
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)


if __name__ == '__main__':
    obj = RandomizedCollection()
    obj.insert(4)
    obj.insert(3)
    obj.insert(4)
    obj.insert(2)
    obj.insert(4)
    obj.remove(4)
    obj.remove(3)
    obj.remove(4)
    obj.remove(4)
