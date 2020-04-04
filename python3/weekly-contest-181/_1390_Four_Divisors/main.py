import math
from typing import List


class Solution:
    def getDivisor(self, num):
        res, cnt = 0, 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                j = num // i
                res += i
                cnt += 1
                if j != i:
                    res += j
                    cnt += 1
        return res if cnt == 4 else 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(self.getDivisor(num) for num in nums)
