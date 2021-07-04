class Solution:
    # de Bruijn sequence
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(cur):
            if len(seen) == target:
                return cur

            for i in range(k):
                # if n == 1, cur[:] isn't expected
                nxt = cur[-n + 1:] + str(i) if n > 1 else str(i)
                if nxt not in seen:
                    seen.add(nxt)
                    res = dfs(cur + str(i))
                    if res:
                        return res
                    seen.remove(nxt)
            return ""

        start, target = '0' * n, k ** n
        seen = {start}
        return dfs(start)
