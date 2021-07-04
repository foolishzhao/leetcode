from typing import List


class Solution:
    def maxBuilding(self, n: int, rs: List[List[int]]) -> int:
        rs.append([1, 0])
        rs.append([n, n - 1])
        rs.sort()

        m, res = len(rs), 0
        for i in range(1, m):
            rs[i][1] = min(rs[i][1], rs[i - 1][1] + rs[i][0] - rs[i - 1][0])
        for i in range(m - 2, -1, -1):
            rs[i][1] = min(rs[i][1], rs[i + 1][1] + rs[i + 1][0] - rs[i][0])

        for i in range(1, m):
            l, hl = rs[i - 1]
            r, hr = rs[i]
            res = max(res, max(hl, hr) + (r - l - abs(hr - hl)) // 2)
        return res
