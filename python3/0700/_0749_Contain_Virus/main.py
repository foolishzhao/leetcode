from typing import List


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        def getVirusArea():
            areas, dangers, walls = list(), list(), list()
            seen = set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in seen:
                        seen.add((i, j))
                        area, danger, wall = [(i, j)], set(), 0
                        q = [(i, j)]
                        while q:
                            u, v = q.pop(0)
                            for du, dv in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                                nu, nv = u + du, v + dv
                                if 0 <= nu < m and 0 <= nv < n:
                                    if grid[nu][nv] == 1 and (nu, nv) not in seen:
                                        seen.add((nu, nv))
                                        q.append((nu, nv))
                                        area.append((nu, nv))
                                    if grid[nu][nv] == 0:
                                        danger.add((nu, nv))
                                        wall += 1
                        areas.append(area)
                        dangers.append(danger)
                        walls.append(wall)
            return areas, dangers, walls

        m, n, res = len(grid), len(grid[0]), 0
        areas, dangers, walls = getVirusArea()
        while areas:
            idx = 0
            for i, danger in enumerate(dangers):
                if len(danger) > len(dangers[idx]):
                    idx = i

            if not dangers[idx]:
                break

            res += walls[idx]
            for i, j in areas[idx]:
                grid[i][j] = -1

            for i, danger in enumerate(dangers):
                if i == idx:
                    continue
                for i, j in danger:
                    grid[i][j] = 1

            areas, dangers, walls = getVirusArea()
        return res


if __name__ == '__main__':
    Solution().containVirus([[1, 1, 1, 0, 0, 0, 0, 0, 0],
                             [1, 0, 1, 0, 1, 1, 1, 1, 1],
                             [1, 1, 1, 0, 0, 0, 0, 0, 0]])
