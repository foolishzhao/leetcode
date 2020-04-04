def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (right - left) // 2 + left
            t = guess(mid)
            if t > 0:
                left = mid + 1
            elif t == 0:
                return mid
            else:
                right = mid - 1
