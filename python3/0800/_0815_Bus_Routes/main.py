from typing import List
import collections


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dt = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for b in route:
                dt[b].add(i)

        seen, q, res = set(), [source], 0
        while q:
            nq = list()
            for b in q:
                if b in seen:
                    continue
                seen.add(b)

                if b == target:
                    return res

                for x in dt[b]:
                    for y in routes[x]:
                        if y not in seen:
                            nq.append(y)
                        routes[x] = list()  # need it to prune
            res += 1
            q = nq
        return -1
