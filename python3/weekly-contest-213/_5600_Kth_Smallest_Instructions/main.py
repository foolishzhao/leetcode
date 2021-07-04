from typing import List
import math


class Solution:
    # If we choose to walk down a row when we have sLeft more steps and rLeft rows left to walk down
    # then we're cutting out the number of combinations of (sLeft - 1) steps with rLeft rows to walk down,
    # because all of those combinations would result in a lexicographically smaller instruction set.
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        r, c = destination
        sLeft, rLeft, res = r + c, r, ""
        for i in range(r + c):
            sLeft -= 1
            com = math.comb(sLeft, rLeft)
            if com >= k:
                res += 'H'
            else:
                res += 'V'
                k -= com
                rLeft -= 1
        return res
