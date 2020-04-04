from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        zCnt = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                zCnt[i + 1][j + 1] = zCnt[i][j + 1] + zCnt[i + 1][j] - zCnt[i][j] + int(grid[i][j] == 0)

        return self.dfs(zCnt, 1, 1, n, n)

    def dfs(self, zCnt, i, j, u, v):
        zeros = zCnt[u][v] - zCnt[i - 1][v] - zCnt[u][j - 1] + zCnt[i - 1][j - 1]
        total = (u - i + 1) * (v - j + 1)
        if zeros == 0:
            return Node(True, True, None, None, None, None)
        elif zeros == total:
            return Node(False, True, None, None, None, None)

        mi, mj = (i + u) >> 1, (j + v) >> 1
        node = Node(False, False, None, None, None, None)
        node.topLeft = self.dfs(zCnt, i, j, mi, mj)
        node.topRight = self.dfs(zCnt, i, mj + 1, mi, v)
        node.bottomLeft = self.dfs(zCnt, mi + 1, j, u, mj)
        node.bottomRight = self.dfs(zCnt, mi + 1, mj + 1, u, v)

        return node


class Solution2:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.dfs(grid, 0, 0, n)

    def dfs(self, grid, x, y, n):
        if n == 1:
            return Node(grid[x][y] == 1, True, None, None)

        nn = n >> 1
        topLeft = self.dfs(grid, x, y, nn)
        topRight = self.dfs(grid, x, y + nn, nn)
        bottomLeft = self.dfs(grid, x + nn, y, nn)
        bottomRight = self.dfs(grid, x + nn, y + nn, nn)

        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and (
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True, None, None)
        else:
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)


if __name__ == '__main__':
    Solution().construct(
        [[1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         ])
