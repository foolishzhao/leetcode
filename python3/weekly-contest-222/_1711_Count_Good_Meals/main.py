from typing import List
import collections


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        tar = set()
        for i in range(22):
            tar.add(1 << i)

        dt, res = collections.defaultdict(int), 0
        for d in deliciousness:
            for t in tar:
                res += dt[t - d]
            dt[d] += 1
        return res % (10 ** 9 + 7)
