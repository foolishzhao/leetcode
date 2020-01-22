from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            n = len(res)
            for i in range(n - 1, 0, -1):
                res[i] += res[i - 1]
            res.append(1)

        return res
