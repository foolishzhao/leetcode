from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(u, v):
            st = set()
            for i in range(u, u + 3):
                for j in range(v, v + 3):
                    if 1 <= grid[i][j] <= 9:
                        st.add(grid[i][j])

            if len(st) != 9:
                return False

            st = {
                grid[u][v] + grid[u + 1][v + 1] + grid[u + 2][v + 2],
                grid[u][v + 2] + grid[u + 1][v + 1] + grid[u + 2][v],
            }
            for i in range(u, u + 3):
                rs = 0
                for j in range(v, v + 3):
                    rs += grid[i][j]
                st.add(rs)

            for i in range(v, v + 3):
                cs = 0
                for j in range(u, u + 3):
                    cs += grid[j][i]
                st.add(cs)

            return len(st) == 1

        m, n = len(grid), len(grid[0])
        return sum([isMagic(i, j) for i in range(m - 2) for j in range(n - 2)])
