from typing import List


class Solution:
    #  Time Limit Exceeded
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n, res = len(seats), len(seats[0]), 0
        visited = [[False] * n for _ in range(m)]

        def valid(i, j):
            if i == 0 and j == 0:
                return True
            elif i == 0:
                # left
                return not visited[i][j - 1]
            elif j == 0:
                # upper right
                return j == n - 1 or not visited[i - 1][j + 1]
            else:
                # left, upper left, upper right
                return not visited[i - 1][j - 1] and not visited[i][j - 1] and (j == n - 1 or not visited[i - 1][j + 1])

        def dfs(pos, curRes):
            nonlocal res
            if pos == m * n:
                res = max(res, curRes)
                return

            i, j = pos // n, pos % n
            if seats[i][j] == '.' and valid(i, j):
                visited[i][j] = True
                dfs(pos + 1, curRes + 1)
                visited[i][j] = False

            dfs(pos + 1, curRes)

        dfs(0, 0)
        return res

    # Bitmasking DP
    def maxStudents2(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        rows = list()
        for i in range(m):
            cur = 0
            for j in range(n):
                cur = (cur << 1) | (seats[i][j] == '.')
            rows.append(cur)

        def countBits(n):
            res = 0
            while n:
                res += 1
                n = n & (n - 1)
            return res

        dp = [[-1] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            row = rows[i - 1]
            for j in range(1 << n):
                if (j & row) == j and not (j & (j >> 1)):
                    for k in range(1 << n):
                        if not (j & (k >> 1)) and not ((j >> 1) & k) and dp[i - 1][k] != -1:
                            dp[i][j] = max(dp[i][j], dp[i - 1][k] + countBits(j))

        return max(dp[-1])


if __name__ == '__main__':
    print(Solution().maxStudents(
        [[".", ".", ".", ".", "#", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", "#", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", "#", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "#", ".", ".", "#", "."]],
    ))
