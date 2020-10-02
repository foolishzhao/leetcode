from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dt1 = dict()
        for i, s in enumerate(list1):
            dt1[s] = i

        dt2 = dict()
        for i, s in enumerate(list2):
            if s in dt1:
                dt2[s] = dt1[s] + i

        minIndex = min(dt2.values())
        return [k for k, v in dt2.items() if v == minIndex]

    def findRestaurant2(self, list1: List[str], list2: List[str]) -> List[str]:
        dt1 = {s: i for i, s in enumerate(list1)}

        res, mIndex = list(), float('inf')
        for i, s in enumerate(list2):
            if s in dt1:
                if i + dt1[s] < mIndex:
                    mIndex = i + dt1[s]
                    res = [s]
                elif i + dt1[s] == mIndex:
                    res.append(s)

        return res
