from typing import List
import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = sorted(list(collections.Counter(arr).values()))
        cur = 0
        for i, c in enumerate(counter):
            cur += c
            if cur > k:
                return len(counter) - i
        return 0
