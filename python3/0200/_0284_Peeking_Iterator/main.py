class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.last = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.last:
            return self.last

        self.last = self.iter.next()
        return self.last

    def next(self):
        """
        :rtype: int
        """
        res = self.last
        self.last = None
        if not res:
            res = self.iter.next()

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        # need to return True/False explicitly
        return True if self.last or self.iter.hasNext() else False
