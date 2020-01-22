from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        visited = {s}
        queue = [s]
        found = False
        while queue:
            cur = queue.pop(0)
            curM = self.mismatch(cur)
            if not curM:
                res.append(cur)
                found = True

            if not found:
                for i, c in enumerate(cur):
                    if c in ('(', ')'):
                        t = cur[:i] + cur[i + 1:]
                        if t not in visited and self.mismatch(t) < curM:
                            visited.add(t)
                            queue.append(t)

        return res

    def removeInvalidParentheses2(self, s: str) -> List[str]:
        res = []
        self.dfs(res, set(), s)
        return res

    def dfs(self, res, visited, s):
        mm = self.mismatch(s)
        if not mm:
            res.append(s)
            return

        for i, c in enumerate(s):
            if c in ('(', ')'):
                t = s[:i] + s[i + 1:]
                if t not in visited and self.mismatch(t) < mm:
                    visited.add(t)
                    self.dfs(res, visited, t)

    def mismatch(self, s: str) -> int:
        a, b = 0, 0
        for c in s:
            if c == '(':
                a += 1
            elif c == ')':
                a -= 1
                if a < 0:
                    b += 1
                    a = 0

        return a + b
