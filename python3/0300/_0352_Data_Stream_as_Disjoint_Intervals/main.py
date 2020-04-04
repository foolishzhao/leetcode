from typing import List


class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        # find first j, i.e. self.intervals[j - 1][0] <= val < self.intervals[j][0]
        if not self.intervals or val > self.intervals[-1][1] + 1:
            self.intervals.append([val, val])
        elif val < self.intervals[0][0] - 1:
            self.intervals.insert(0, [val, val])
        elif val == self.intervals[-1][1] + 1:
            self.intervals[-1][1] += 1
        elif val == self.intervals[0][0] - 1:
            self.intervals[0][0] -= 1
        else:
            j = 1
            while j < len(self.intervals) and val >= self.intervals[j][0]:
                j += 1

            if j < len(self.intervals):
                if self.intervals[j - 1][1] + 1 < val < self.intervals[j][0] - 1:
                    self.intervals.insert(j, [val, val])
                elif self.intervals[j - 1][1] + 1 == val == self.intervals[j][0] - 1:
                    self.intervals[j - 1][1] = self.intervals[j][1]
                    self.intervals.pop(j)
                elif val == self.intervals[j - 1][1] + 1:
                    self.intervals[j - 1][1] += 1
                elif val == self.intervals[j][0] - 1:
                    self.intervals[j][0] -= 1

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# use sentinel
class SummaryRanges2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # corner case: coz -1 can merge with 0, so using -2 instead
        self.intervals = [[-2, -2], [1 << 32, 1 << 32]]

    # O(n)
    def addNum(self, val: int) -> None:
        # find first j, i.e. self.intervals[j - 1][0] <= val < self.intervals[j][0]
        j = 1
        while j < len(self.intervals) and val >= self.intervals[j][0]:
            j += 1

        if j < len(self.intervals):
            if self.intervals[j - 1][1] + 1 < val < self.intervals[j][0] - 1:
                self.intervals.insert(j, [val, val])
            elif self.intervals[j - 1][1] + 1 == val == self.intervals[j][0] - 1:
                self.intervals[j - 1][1] = self.intervals[j][1]
                self.intervals.pop(j)
            elif val == self.intervals[j - 1][1] + 1:
                self.intervals[j - 1][1] += 1
            elif val == self.intervals[j][0] - 1:
                self.intervals[j][0] -= 1

    # O(1)
    def getIntervals(self) -> List[List[int]]:
        return self.intervals[1:-1]


# When addNum is much more frequent than getIntervals
class SummaryRanges3:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    # O(1)
    def addNum(self, val: int) -> None:
        self.intervals.append([val, val])

    # O(n*log(n))
    def getIntervals(self) -> List[List[int]]:
        self.intervals.sort(key=lambda x: x[0])

        res = [[-2, -2]]
        for x, y in self.intervals:
            if x > res[-1][1] + 1:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)

        self.intervals = res[1:]
        return self.intervals
