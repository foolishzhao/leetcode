import collections
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n, cnts = len(nums), [collections.Counter(nums[i::k]) for i in range(k)]

        # # choose k numbers

        # more that one not from nums -> impossible

        # one num not from nums -> n - (sum(mxs) - min(mxs))
        mxs = [c.most_common(1)[0][1] for c in cnts]

        # all num from nums -> n - d1[0]
        d1 = cnts[0]
        for i in range(1, k):
            d2 = collections.defaultdict(int)
            for x in d1:
                for y in cnts[i]:
                    t = x ^ y
                    d2[t] = max(d2[t], d1[x] + cnts[i][y])
            d1 = d2
        return min(n - (sum(mxs) - min(mxs)), n - d1[0])
