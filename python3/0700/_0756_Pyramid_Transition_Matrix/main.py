from typing import List
import collections
import itertools


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        dt = collections.defaultdict(lambda: collections.defaultdict(list))
        for u, v, w in allowed:
            dt[u][v].append(w)

        def dfs(x):
            if len(x) == 1:
                return True
            return any(dfs(y) for y in itertools.product(*(dt[u][v] for u, v in zip(x[:-1], x[1:]))))

        return dfs(bottom)


if __name__ == '__main__':
    print(Solution().pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]))
