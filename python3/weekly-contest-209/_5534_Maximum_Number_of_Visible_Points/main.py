from typing import List
import bisect
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        dup, angles = 0, list()

        px, py = location[0], location[1]
        for x, y in points:
            if x == px and y == py:
                dup += 1
            else:
                angles.append(math.atan2(y - py, x - px) * 180 / math.pi)
        angles.sort()

        res, n = dup, len(angles)
        if n:
            for i in range(n):
                angles.append(angles[i] + 360)

            i, j = 0, bisect.bisect_right(angles, angles[0] + angle)
            while i < n:
                res = max(res, dup + j - i)
                i += 1

                while j < 2 * n and angles[j] - angles[i] <= angle:
                    j += 1

        return res


if __name__ == '__main__':
    Solution().visiblePoints(
        [[2, 1], [2, 2], [3, 3]],
        90,
        [1, 1],
    )
