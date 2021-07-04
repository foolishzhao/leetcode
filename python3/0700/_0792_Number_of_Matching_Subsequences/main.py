from typing import List
import collections
import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubseq(word):
            i = 0
            for w in word:
                idx = bisect.bisect_left(dt[w], i)
                if idx == len(dt[w]):
                    return False
                i = dt[w][idx] + 1
            return True

        dt = collections.defaultdict(list)
        for i, c in enumerate(s):
            dt[c].append(i)

        return sum([isSubseq(word) for word in words])
