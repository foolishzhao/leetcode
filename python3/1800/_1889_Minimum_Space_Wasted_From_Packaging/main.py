from typing import List
import bisect


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()

        n, res, ps = len(packages), float('inf'), sum(packages)
        for box in boxes:
            box.sort()
            if packages[-1] > box[-1]:
                continue

            i, bs = 0, 0
            for b in box:
                if i == n:
                    break

                j = bisect.bisect_right(packages, b, i)
                bs += b * (j - i)
                i = j

            res = min(res, bs - ps)

        return -1 if res == float('inf') else res % (10 ** 9 + 7)
