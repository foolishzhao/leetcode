import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 10
        for c in s:
            if c == 'z':
                count[0] += 1
            elif c == 'o':
                count[1] += 1
            elif c == 'w':
                count[2] += 1
            elif c == 'h':
                count[3] += 1
            elif c == 'u':
                count[4] += 1
            elif c == 'f':
                count[5] += 1
            elif c == 'x':
                count[6] += 1
            elif c == 's':
                count[7] += 1
            elif c == 'g':
                count[8] += 1
            elif c == 'i':
                count[9] += 1

        count[1] -= count[0] + count[2] + count[4]
        count[3] -= count[8]
        count[5] -= count[4]
        count[7] -= count[6]
        count[9] -= count[5] + count[6] + count[8]

        res = ""
        for i, v in enumerate(count):
            for _ in range(v):
                res += str(i)
        return res
