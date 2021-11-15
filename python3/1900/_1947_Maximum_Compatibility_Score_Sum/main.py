from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def score(i, j):
            return sum([x == y for x, y in zip(students[i], mentors[j])])

        def dfs(curScore, curPos):
            if curPos == m:
                return curScore

            res = 0
            for j in range(m):
                if j not in seen:
                    seen.add(j)
                    res = max(res, dfs(curScore + score(curPos, j), curPos + 1))
                    seen.remove(j)
            return res

        m, n = len(students), len(students[0])
        seen = set()
        return dfs(0, 0)
