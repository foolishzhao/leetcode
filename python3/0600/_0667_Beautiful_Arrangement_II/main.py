from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n - k))
        l, r = n - k, n
        while l <= r:
            res.append(l)
            l += 1
            if l <= r:
                res.append(r)
                r -= 1
        return res
