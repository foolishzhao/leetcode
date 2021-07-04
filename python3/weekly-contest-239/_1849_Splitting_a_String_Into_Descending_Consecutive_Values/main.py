class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(s, prev, cur):
            if cur == len(s):
                return prev and int(s) + 1 == prev

            if dfs(s, prev, cur + 1):
                return True

            if prev is None or int(s[:cur]) + 1 == prev:
                return dfs(s[cur:], int(s[:cur]), 1)

            return False

        return dfs(s, None, 1)
