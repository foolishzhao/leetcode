from typing import List
import collections


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dt = collections.defaultdict(int)
        for w in words:
            for c in w:
                dt[c] += 1

        for v in dt.values():
            if v % len(words) != 0:
                return False
        return True
