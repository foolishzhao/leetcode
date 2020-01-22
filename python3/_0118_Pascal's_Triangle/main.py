from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        res, prev = [[1]], []
        for _ in range(numRows - 1):
            cur = [1]
            for j in range(1, len(prev)):
                cur.append(prev[j - 1] + prev[j])
            cur.append(1)

            res.append(cur)
            prev = cur

        return res
