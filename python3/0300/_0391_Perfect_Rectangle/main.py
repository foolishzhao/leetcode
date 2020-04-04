from typing import List
import heapq
import bisect


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        n, area = len(rectangles), 0
        x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        st = set()
        for rec in rectangles:
            x1 = min(x1, rec[0])
            y1 = min(y1, rec[1])
            x2 = max(x2, rec[2])
            y2 = max(y2, rec[3])

            area += (rec[3] - rec[1]) * (rec[2] - rec[0])

            for x, y in [(rec[0], rec[1]), (rec[0], rec[3]), (rec[2], rec[1]), (rec[2], rec[3])]:
                if (x, y) in st:
                    st.remove((x, y))
                else:
                    st.add((x, y))

        if area != (y2 - y1) * (x2 - x1):
            return False

        if len(st) != 4 or (x1, y1) not in st or (x1, y2) not in st or (x2, y1) not in st or (x2, y2) not in st:
            return False

        return True

    # condition1: equal area
    # condition2: no overlap
    def isRectangleCover2(self, rectangles: List[List[int]]) -> bool:
        n, area = len(rectangles), 0
        x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        pq = list()
        for rec in rectangles:
            x1 = min(x1, rec[0])
            y1 = min(y1, rec[1])
            x2 = max(x2, rec[2])
            y2 = max(y2, rec[3])

            area += (rec[3] - rec[1]) * (rec[2] - rec[0])

            heapq.heappush(pq, (rec[0], 1, rec[1], rec[3]))
            heapq.heappush(pq, (rec[2], -1, rec[1], rec[3]))

        if area != (y2 - y1) * (x2 - x1):
            return False

        yRange = list()
        while pq:
            _, t, yb, yt = heapq.heappop(pq)
            if t < 0:
                yRange.remove((yb, yt))
            else:
                i = bisect.bisect_left(yRange, (yb, yt))
                if i > 0 and yRange[i - 1][1] > yb:
                    return False
                if i < len(yRange) and yRange[i][0] < yt:
                    return False

                bisect.insort_left(yRange, (yb, yt))

        return True


if __name__ == '__main__':
    Solution().isRectangleCover2([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]])
