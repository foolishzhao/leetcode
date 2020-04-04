from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        maxColVal = [max(matrix[i][j] for i in range(m)) for j in range(n)]

        res = list()
        for i in range(m):
            minRowVal = min(matrix[i])
            for j in range(n):
                if matrix[i][j] == minRowVal and maxColVal[j] == minRowVal:
                    res.append(minRowVal)

        return res
