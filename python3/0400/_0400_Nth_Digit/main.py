class Solution:
    def findNthDigit(self, n: int) -> int:
        length, count, cur = 1, 9, 1
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            cur *= 10

        cur += (n - 1) // length
        return int(str(cur)[(n - 1) % length])
