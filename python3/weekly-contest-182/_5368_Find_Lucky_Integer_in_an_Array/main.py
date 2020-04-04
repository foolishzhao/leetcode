from typing import List
import collections


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dt = collections.defaultdict(int)
        for num in arr:
            dt[num] += 1

        res = -1
        for num, cnt in dt.items():
            if num == cnt:
                res = max(res, num)
        return res
