import bisect
from collections import deque


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = list()
        self.sorted = list()

    # O(log(m))
    def addElement(self, num: int) -> None:
        self.nums.append(num)
        bisect.insort(self.sorted, num)

        if len(self.nums) > self.m:
            x = self.nums[0]
            self.nums = self.nums[1:]
            idx = bisect.bisect_left(self.sorted, x)
            self.sorted = self.sorted[:idx] + self.sorted[idx + 1:]

    # O(k)
    def calculateMKAverage(self) -> int:
        if len(self.nums) < self.m:
            return -1

        return sum(self.sorted[self.k: self.m - self.k]) // (self.m - 2 * self.k)


class BIT:
    def __init__(self, n):
        self.nums = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.nums):
            self.nums[i] += delta
            i += i & -i

    def sum(self, i):
        res, i, = 0, i + 1
        while i:
            res += self.nums[i]
            i -= i & -i
        return res


class MKAverage2:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = deque()
        self.value = BIT(10 ** 5)
        self.index = BIT(10 ** 5)

    def addElement(self, num: int) -> None:
        self.nums.append(num)
        self.value.update(num, num)
        self.index.update(num, 1)
        if len(self.nums) > self.m:
            num = self.nums.popleft()
            self.value.update(num, -num)
            self.index.update(num, -1)

    def calculateMKAverage(self) -> int:
        if len(self.nums) < self.m:
            return -1

        # exactly kth index
        def getIndex(k):
            lo, hi = 0, 10 ** 5
            while lo < hi:
                mi = lo + hi >> 1
                if self.index.sum(mi) < k:
                    lo = mi + 1
                else:
                    hi = mi
            return lo

        lo = getIndex(self.k)
        hi = getIndex(self.m - self.k)
        # self.value.sum(hi): sum of all num <= hi, we only want to include 1st num == hi
        # self.value.sum(lo): sum of all num <= lo, we only want to include 1st num == lo
        res = self.value.sum(hi) - self.value.sum(lo)
        res += (self.index.sum(lo) - self.k) * lo
        res -= (self.index.sum(hi) - (self.m - self.k)) * hi
        return res // (self.m - self.k * 2)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
