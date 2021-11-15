import functools


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def checkState(state):
            return all(x != y for x, y in zip(state[:-1], state[1:]))

        def checkNextState(cur, nxt):
            return all(x != y for x, y in zip(cur, nxt))

        def product(colors, r):
            def dfs(curRes, i):
                nonlocal res
                if i == 0:
                    res.append(curRes)
                    return

                for c in colors:
                    dfs(curRes + c, i - 1)

            res = list()
            dfs('', r)
            return res

        mod = 10 ** 9 + 7
        states = [x for x in product('RGB', m) if checkState(x)]
        nextStates = {x: [y for y in states if checkNextState(x, y)] for x in states}

        @functools.lru_cache(None)
        def dp(x, i):
            if i == 0:
                return 1

            return sum([dp(y, i - 1) for y in nextStates[x]]) % mod

        return sum([dp(x, n - 1) for x in states]) % mod
