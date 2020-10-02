from typing import List
import functools


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(remain):
            li = eval(remain)
            if sum(li) == 0:
                return 0

            res = sum(l * p for l, p in zip(li, price))
            for s in special:
                r = [x - y for x, y in zip(li, s[:-1])]
                if min(r) >= 0:
                    res = min(res, s[-1] + dp(str(r)))

            return res

        return dp(str(needs))
