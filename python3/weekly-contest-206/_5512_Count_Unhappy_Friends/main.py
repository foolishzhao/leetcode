from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dt = dict()
        for x, y in pairs:
            dt[x] = y
            dt[y] = x

        res = 0
        for x in range(n):
            y, unhappy = dt[x], False
            for u in preferences[x]:
                if unhappy:
                    break

                if u == y:
                    break

                v = dt[u]
                for p in preferences[u]:
                    if p == x or p == v:
                        unhappy = p == x
                        break
            res += unhappy

        return res
