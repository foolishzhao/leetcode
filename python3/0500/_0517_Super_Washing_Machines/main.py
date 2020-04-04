from typing import List


class Solution:
    # maximum number of necessary operations on every machine
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if sum(machines) % n:
            return -1

        avg = sum(machines) // n
        for i in range(n):
            machines[i] -= avg

        res, leftSum = 0, 0
        for i, v in enumerate(machines):
            rightSum = -leftSum - v
            if leftSum < 0 and rightSum < 0:
                res = max(res, -leftSum - rightSum)
            else:
                res = max(res, max(abs(leftSum), abs(rightSum)))
            leftSum += v
        return res
