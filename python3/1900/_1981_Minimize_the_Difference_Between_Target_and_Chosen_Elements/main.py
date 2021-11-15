from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        mn = sum([min(row) for row in mat])
        if mn > target:
            return mn - target

        st = {0}
        for row in mat:
            st = {x + y for x in row for y in st if x + y <= (2 * target - mn)}
        return min([abs(x - target) for x in st])

    def minimizeTheDifference2(self, mat: List[List[int]], target: int) -> int:
        for row in mat:
            row.sort()

        st = {0}
        for row in mat:
            newSt = set()
            for x in st:
                for y in row:
                    newSt.add(x + y)
                    if x + y >= target:
                        break
            st = newSt

        return min([abs(x - target) for x in st])
