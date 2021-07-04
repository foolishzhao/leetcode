from typing import List
import collections


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter, res = collections.Counter(answers), 0
        for answer, cnt in counter.items():
            res += ((cnt - 1) // (answer + 1) + 1) * (answer + 1)
        return res
