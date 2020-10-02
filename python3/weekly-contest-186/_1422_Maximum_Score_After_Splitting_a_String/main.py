class Solution:
    def maxScore(self, s: str) -> int:
        res, n = 0, len(s)
        for i in range(1, n):
            res = max(res, s[:i].count('0') + s[i:].count('1'))
        return res

    def maxScore2(self, s: str) -> int:
        n = len(s)

        leftZ = [0] * n
        for i in range(1, n):
            leftZ[i] = leftZ[i - 1]
            if s[i - 1] == '0':
                leftZ[i] += 1

        rightO = [0] * n
        for i in range(n - 2, -1, -1):
            rightO[i] = rightO[i + 1]
            if s[i + 1] == '1':
                rightO[i] += 1

        res = 0
        for i in range(1, n):
            res = max(res, leftZ[i] + rightO[i - 1])
        return res

    def maxScore3(self, s: str) -> int:
        res, c0, c1 = 0, 0, s.count('1')
        for i in range(len(s) - 1):
            if s[i] == '0':
                c0 += 1
            else:
                c1 -= 1
            res = max(res, c0 + c1)
        return res
