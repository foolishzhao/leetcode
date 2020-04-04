from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        if not s:
            return res

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i > 0 and s[i - 1] == s[i]:
                dp[i - 1][i] = True

        for k in range(2, n):
            for i in range(0, n - k):
                if dp[i + 1][i + k - 1] and s[i] == s[i + k]:
                    dp[i][i + k] = True

        self.dfs(res, [], dp, s, 0, n)
        return res

    def dfs(self, res: List[List[str]], curRes: List[str], dp: List[List[bool]], s: str, pos: int, n: int):
        if pos == n:
            res.append(curRes)
            return

        for j in range(pos, n):
            if dp[pos][j]:
                self.dfs(res, curRes + [s[pos:j + 1]], dp, s, j + 1, n)


if __name__ == '__main__':
    Solution().partition("aab")
