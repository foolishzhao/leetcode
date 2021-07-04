from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n, res = len(grid), len(grid[0]), list()
        for i in range(n):
            curX, curY, curD = 0, i, 0
            while True:
                if curD == 0:
                    nextX, nextY = curX, curY + grid[curX][curY]
                    if nextY == n or nextY < 0 or grid[nextX][nextY] != grid[curX][curY]:
                        res.append(-1)
                        break
                    curX, curY, curD = nextX, nextY, 1 - curD
                else:
                    nextX, nextY = curX + 1, curY
                    if nextX == m:
                        res.append(curY)
                        break
                    curX, curY, curD = nextX, nextY, 1 - curD
        return res

    def findBall2(self, grid: List[List[int]]) -> List[int]:
        def helper(j):
            for i in range(m):
                nj = j + grid[i][j]
                if nj < 0 or nj == n or grid[i][j] != grid[i][nj]:
                    return -1
                j = nj
            return j

        m, n = len(grid), len(grid[0])
        return [helper(j) for j in range(n)]
