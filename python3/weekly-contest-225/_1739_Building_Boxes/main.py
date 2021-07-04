class Solution:
    def minimumBoxes(self, n: int) -> int:
        touch, cur, total, res = 1, 1, 1, 1
        while total < n:
            touch += 1
            cur += touch
            total += cur
            res += touch

        while total >= n:
            total -= touch
            touch -= 1
            res -= 1

        return res + 1
