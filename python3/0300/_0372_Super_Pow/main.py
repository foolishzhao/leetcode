from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        
        return self.powHelper(self.superPow(a, b[:-1]), 10) * self.powHelper(a, b[-1]) % 1337

    def powHelper(self, a, b):
        a %= 1337
        res = 1
        for i in range(b):
            res *= a
            res %= 1337

        return res
