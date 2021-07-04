from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        prev, cur, res = -2, -1, 0
        # sort by end
        for lo, hi in sorted(intervals, key=lambda x: x[1]):
            if lo <= prev:
                continue
            elif lo <= cur:
                prev, cur = cur, hi
                if prev == cur:
                    prev -= 1
                res += 1
            else:
                prev, cur = hi - 1, hi
                res += 2
        return res


if __name__ == '__main__':
    Solution().intersectionSizeTwo(
        [[1, 3], [3, 7], [5, 7], [7, 8]],
    )
