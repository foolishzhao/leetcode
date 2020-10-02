class Solution:
    def minFlips(self, target: str) -> int:
        target = '0' + target
        res, n = 0, len(target)
        for i in range(1, n):
            res += target[i] != target[i - 1]
        return res
