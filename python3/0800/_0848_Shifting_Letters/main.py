from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n, s = len(shifts), list(s)

        shifts[-1] %= 26
        for i in range(n - 1, 0, -1):
            shifts[i - 1] += shifts[i]
            shifts[i - 1] %= 26

        for i in range(n):
            if ord(s[i]) + shifts[i] > ord('z'):
                s[i] = chr(ord(s[i]) + shifts[i] - ord('z') + ord('a') - 1)
            else:
                s[i] = chr(ord(s[i]) + shifts[i])

        return ''.join(s)

    def shiftingLetters2(self, s: str, shifts: List[int]) -> str:
        n, s = len(shifts), list(s)

        shifts[-1] %= 26
        for i in range(n - 1, 0, -1):
            shifts[i - 1] += shifts[i]
            shifts[i - 1] %= 26

        for i in range(n):
            s[i] = chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
        return ''.join(s)
