class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxZeros, maxOnes = 0, 0
        prev, curLen = None, 0

        for c in s + '2':
            if c == prev:
                curLen += 1
            else:
                if prev == '0':
                    maxZeros = max(maxZeros, curLen)
                elif prev == '1':
                    maxOnes = max(maxOnes, curLen)
                curLen = 1
            prev = c
        return maxOnes > maxZeros

    def checkZeroOnes2(self, s: str) -> bool:
        maxOnes = max([len(x) for x in s.split('0')])
        maxZeros = max([len(x) for x in s.split('1')])
        return maxOnes > maxZeros
