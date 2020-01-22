from typing import List


# https://www.cnblogs.com/whensean/p/6851018.html
# https://blog.csdn.net/Yaokai_AssultMaster/article/details/79492190
class BinaryIndexTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        nums.insert(0, 0)
        for i in range(1, n + 1):
            j = i + i & (-i)
            if j <= n:
                nums[j] += nums[i]

        self.bitArr = nums
        self.n = n

    def sumPrefix(self, i: int) -> int:
        i += 1
        if i > self.n:
            return -1

        res = 0
        while i:
            res += self.bitArr[i]
            i -= i & -i

        return res

    def sumRange(self, i: int, j: int) -> int:
        return self.sumPrefix(j) - self.sumPrefix(i - 1)

    def update(self, idx: int, delta: int):
        idx += 1
        while idx <= self.n:
            self.bitArr[idx] += delta
            idx += idx & (-idx)


if __name__ == '__main__':
    bit = BinaryIndexTree([1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5])
    print(bit.sumPrefix(2))
    print(bit.sumPrefix(4))
    print(bit.sumRange(2, 4))
    bit.update(1, -3)
    print(bit.sumPrefix(2))
