from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        n, res = len(points), 0
        inf = (0, 0)
        for i in range(n):
            dup = 1
            dt = {}
            u = points[i]
            for j in range(i + 1, n):
                v = points[j]
                if u[0] == v[0] and u[1] == v[1]:
                    dup += 1
                elif u[0] == v[0]:
                    dt[inf] = dt.get(inf, 0) + 1
                else:
                    gcd = self.gcd(u[1] - v[1], u[0] - v[0])
                    t = ((u[1] - v[1]) // gcd, (u[0] - v[0]) // gcd)
                    dt[t] = dt.get(t, 0) + 1

            # in case all points at one point
            res = max(res, dup)
            for k in dt:
                res = max(res, dt[k] + dup)

        return res

    def gcd(self, x: int, y: int) -> int:
        # incorrect if x == 0, but y < 0
        # if x > y:
        #     return self.gcd(y, x)
        return y if not x else self.gcd(y % x, x)


if __name__ == '__main__':
    print(Solution().gcd(-3, -6))
    print(Solution().gcd(-3, 6))
