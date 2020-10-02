class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and ((j - i < 2) or dp[i + 1][j - 1])
                res += dp[i][j]
        return res

    def countSubstrings2(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.helper(s, i, i)
            res += self.helper(s, i, i + 1)
        return res

    def helper(self, s, l, r):
        res = 0
        while 0 <= l and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    def countSubstrings3(self, s: str) -> int:
        s = '^#' + '#'.join(s) + '#$'
        L, n, c, r = [0] * len(s), len(s), 0, 0
        for i in range(n):
            if r > i:
                L[i] = min(r - i, L[2 * c - i])
            while L[i] <= i < n - L[i] and s[i + L[i]] == s[i - L[i]]:
                L[i] += 1
            if i + L[i] > r:
                c, r = i, i + L[i]

        return sum([l // 2 for l in L])

    def countSubstrings4(self, s: str) -> int:
        s = '^#' + '#'.join(s) + '#$'
        L, n, c, r = [0] * len(s), len(s), 0, 0
        for i in range(1, n - 1):
            if r > i:
                L[i] = min(r - i, L[2 * c - i])
            # no need index check as we already limit i to 1 ~ n - 2
            while s[i + L[i]] == s[i - L[i]]:
                L[i] += 1
            if i + L[i] > r:
                c, r = i, i + L[i]

        return sum([l // 2 for l in L])


if __name__ == '__main__':
    Solution().countSubstrings3("abc")
