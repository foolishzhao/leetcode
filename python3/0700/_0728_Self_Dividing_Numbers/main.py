from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right + 1) if self.isDividing(x)]

    def isDividing(self, num):
        cur = num
        while cur:
            d = cur % 10
            cur //= 10
            if not d or num % d:
                return False
        return True
