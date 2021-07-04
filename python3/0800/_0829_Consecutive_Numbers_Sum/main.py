class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res, k = 1, 2
        while True:
            t = n - k * (k - 1) // 2
            if t <= 0:
                break

            res += t % k == 0
            k += 1
        return res
