from typing import List
from itertools import product


class Solution:
    def earliestAndLatest(self, n: int, F: int, S: int) -> List[int]:
        def dfs(player, r):
            pairs, m = list(), len(player)
            for i in range(m // 2):
                x, y = player[i], player[-i - 1]
                if (x, y) == (F, S):
                    rs.add(r)
                    return

                if x not in (F, S) and y not in (F, S):
                    pairs.append((x, y))

            add = (F, S) if m % 2 == 0 else tuple({F, S, player[m // 2]})
            for np in product(*pairs):
                dfs(sorted(np + add), r + 1)

        rs = set()
        dfs(list(range(1, n + 1)), 1)
        return [min(rs), max(rs)]
