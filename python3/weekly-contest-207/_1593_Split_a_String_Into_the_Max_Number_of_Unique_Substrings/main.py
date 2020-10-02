class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(pos, visited):
            if pos == n:
                return 0

            res = -1
            for i in range(pos + 1, n + 1):
                cur = s[pos: i]
                if cur not in visited:
                    visited.add(cur)
                    subRes = dfs(i, visited)
                    if subRes != -1:
                        res = max(res, subRes + 1)
                    visited.remove(cur)
            return res

        n = len(s)
        return dfs(0, set())
