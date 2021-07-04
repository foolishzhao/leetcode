class Solution:
    def minSwaps(self, s: str) -> int:
        zeroCnt, oneCnt = s.count('0'), s.count('1')
        if abs(zeroCnt - oneCnt) > 1:
            return -1

        def compare(s1, s2):
            res = 0
            for x, y in zip(s1, s2):
                res += x != y
            return res

        if zeroCnt == oneCnt:
            return min(compare(s, '01' * zeroCnt), compare(s, '10' * oneCnt)) // 2
        elif zeroCnt > oneCnt:
            return compare(s, '01' * oneCnt + '0') // 2
        else:
            return compare(s, '10' * zeroCnt + '1') // 2

    def minSwaps2(self, s: str) -> int:
        zeroCnt, oneCnt = s.count('0'), s.count('1')
        if abs(zeroCnt - oneCnt) > 1:
            return -1

        def swap(s1, c):
            res = 0
            for c1 in s1:
                if int(c1) != c:
                    res += 1
                c ^= 1
            return res // 2

        if zeroCnt == oneCnt:
            return min(swap(s, 0), swap(s, 1))
        elif zeroCnt > oneCnt:
            return swap(s, 0)
        else:
            return swap(s, 1)
