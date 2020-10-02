from typing import List
import collections


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food, dt = set(), dict()
        for _, t, f in orders:
            food.add(f)
            if t not in dt:
                dt[t] = collections.defaultdict(int)
            dt[t][f] += 1

        tables = sorted(list(dt.keys()), key=int)
        food = sorted(list(food))

        res = list()
        res.append(["Table"] + food.copy())
        for t in tables:
            curRes = [t]
            for f in food:
                curRes.append(str(dt[t][f]))
            res.append(curRes)
        return res
