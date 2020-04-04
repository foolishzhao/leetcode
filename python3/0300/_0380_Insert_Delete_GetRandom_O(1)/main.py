import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.index = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.index:
            self.index[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.index:
            index, lastVal = self.index[val], self.nums[-1]
            self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
            self.nums.pop()
            self.index[lastVal] = index
            del self.index[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)
