from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res, cur = list(), 1
        for x in target:
            while cur < x:
                res.append("Push")
                res.append("Pop")
                cur += 1
            res.append("Push")
            cur += 1
        return res
