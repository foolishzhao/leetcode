import collections
from typing import List


class Solution:
    # if don't consider the multiples of 3.
    # Alice starts with mod1, Alice and Bob have to pick 1,1,2,1,2,1... in order.
    # Alice starts with mod2, Alice and Bob have to pick 2,2,1,2,1,2... in order.
    def stoneGameIX(self, stones: List[int]) -> bool:
        mod = collections.Counter([x % 3 for x in stones])
        if mod[0] % 2 == 0:
            return min(mod[1], mod[2]) > 0  # Alice starts with smaller of mod1, mode2
        else:
            return abs(mod[1] - mod[2]) > 2  # Alice starts with bigger of mod1, mode2
