from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        res, curRes = list(), list()
        for i in range(m):
            for j in range(n):
                curRes.append(nums[i][j])
                if len(curRes) == c:
                    res.append(curRes)
                    curRes = list()
        return res

    def matrixReshape2(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        res = [[0] * c for _ in range(r)]
        for i in range(m * n):
            res[i // c][i % c] = nums[i // n][i % n]
        return res
