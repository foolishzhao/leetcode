from bisect import bisect_left, bisect_right


class RangeModule:

    def __init__(self):
        self.nums = list()

    # four cases, suppose nums: [1 3 6 10]
    #   case 1: 5 12
    #   case 2: 5 9
    #   case 3: 2 12
    #   case 4: 2 9

    # use bisect_left to locate left border, bisect_right to locate right border
    #   to avoid value repeat in nums, will cause trouble when query
    def addRange(self, left: int, right: int) -> None:
        i, j = bisect_left(self.nums, left), bisect_right(self.nums, right)
        self.nums[i: j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    # use bisect_right to locate left border
    # use bisect_left to locate right border
    def queryRange(self, left: int, right: int) -> bool:
        i, j = bisect_right(self.nums, left), bisect_left(self.nums, right)
        return i == j and (i % 2 == 1)

    def removeRange(self, left: int, right: int) -> None:
        i, j = bisect_left(self.nums, left), bisect_right(self.nums, right)
        self.nums[i: j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)


if __name__ == '__main__':
    obj = RangeModule()
    obj.addRange(6, 8)
    obj.removeRange(7, 8)
    obj.removeRange(8, 9)
    obj.addRange(8, 9)
    obj.removeRange(1, 3)
    obj.addRange(1, 8)
    print(obj.queryRange(2, 4))
    print(obj.queryRange(2, 9))
    print(obj.queryRange(4, 6))
