from typing import List


class Solution:
    # Always pick the interval with the earliest end time to get the maximal number of non-overlapping intervals.
    # As interval with the earliest end time produces the maximal capacity to hold rest intervals.

    # The longest chain must contain pairs[0].
    # If it doesn't, suppose the longest chain C starts at pairs[k], k > 0.
    # We can always form a new chain C' by replacing pairs[k] with pairs[0], whose length no shorter than C.
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prev, res = float('-inf'), 0
        for x, y in pairs:
            if x > prev:
                prev = y
                res += 1
        return res
