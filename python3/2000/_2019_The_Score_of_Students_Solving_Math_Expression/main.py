from typing import List
import functools


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i == j:
                return {int(s[i])}

            partCorrect = set()
            for k in range(i + 1, j, 2):
                for x in dp(i, k - 1):
                    for y in dp(k + 1, j):
                        t = x * y if s[k] == '*' else x + y
                        if t <= 1000:
                            partCorrect.add(t)
            return partCorrect

        partCorrect, correct = dp(0, len(s) - 1), eval(s)
        res = 0
        for ans in answers:
            if ans == correct:
                res += 5
            elif ans in partCorrect:
                res += 2
        return res
