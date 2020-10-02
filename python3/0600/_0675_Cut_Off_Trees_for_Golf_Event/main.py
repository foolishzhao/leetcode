from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        targets = sorted([forest[i][j] for i in range(m) for j in range(n) if forest[i][j] > 1])

        def minStep(si, sj, target):
            res, q, visited = 0, [(si, sj)], {(si, sj)}
            while q:
                sz = len(q)
                for _ in range(sz):
                    i, j = q.pop(0)
                    if forest[i][j] == target:
                        return i, j, res
                    for mi, mj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + mi, j + mj
                        if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and forest[ni][nj] > 0:
                            q.append((ni, nj))
                            visited.add((ni, nj))
                res += 1
            return -1, -1, -1

        ci, cj, res = 0, 0, 0
        for target in targets:
            ci, cj, cr = minStep(ci, cj, target)
            if cr == -1:
                return -1
            res += cr
        return res
