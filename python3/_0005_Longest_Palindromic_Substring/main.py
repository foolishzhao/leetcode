class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        ps = self.preProcess(s)
        n = len(ps)
        radius = [0] * n
        i, longest = 0, 0
        for j in range(n):
            r = min(longest - j, radius[2 * i - j])
            while j - r >= 0 and j + r < n and ps[j - r] == ps[j + r]:
                r += 1

            radius[j] = r
            if j + r > longest:
                longest = j + r
                i = j

        i, max_radius = 0, radius[0]
        for j in range(n):
            if radius[j] > max_radius:
                max_radius = radius[j]
                i = j

        return s[(i - max_radius) // 2: (i + max_radius) // 2 - 1]

    def preProcess(self, s: str) -> str:
        res = "^#"
        for c in s:
            res += c + "#"
        res += "$"

        return res

    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        for k in range(2, n):
            for i in range(n - k):
                if dp[i + 1][i + k - 1] and s[i] == s[i + k]:
                    dp[i][i + k] = True

        max_start, max_len = 0, 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_start = i

        return s[max_start: max_start + max_len]


if __name__ == '__main__':
    Solution().longestPalindrome("babad")
