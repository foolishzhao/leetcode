from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[[-1] * n for _ in range(n)] for _ in range(2 * n)]
        return self.search(graph, dp, 0, 1, 2)

    def search(self, graph, dp, t, x, y):
        if x == 0:
            return 1
        if y == x:
            return 2
        if t == 2 * len(graph):
            return 0
        if dp[t][x][y] != -1:
            return dp[t][x][y]

        s = t % 2
        if s == 0:
            flag = True
            for nx in graph[x]:
                subRes = self.search(graph, dp, t + 1, nx, y)
                if subRes == 1:
                    dp[t][x][y] = 1
                    return 1
                elif subRes == 0:
                    flag = False

            if flag:
                dp[t][x][y] = 2
            else:
                dp[t][x][y] = 0
            return dp[t][x][y]
        else:
            flag = True
            for ny in graph[y]:
                if ny:
                    subRes = self.search(graph, dp, t + 1, x, ny)
                    if subRes == 2:
                        dp[t][x][y] = 2
                        return 2
                    elif subRes == 0:
                        flag = False

            if flag:
                dp[t][x][y] = 1
            else:
                dp[t][x][y] = 0
            return dp[t][x][y]
