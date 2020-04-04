class Solution:
    # Time Limit Exceeded
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        s1 *= n1
        i, n, cnt = 0, len(s2), 0
        for c in s1:
            if c == s2[i]:
                i += 1
                if i == n:
                    cnt += 1
                    i = 0

        return cnt // n2

    def getMaxRepetitions2(self, s1: str, n1: int, s2: str, n2: int) -> int:
        nextIndex = [0] * (n1 + 1)
        repeatCnt = [0] * (n1 + 1)

        k, j, cnt = 1, 0, 0
        while k <= n1:
            for c in s1:
                if c == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        cnt += 1

            repeatCnt[k] = cnt
            nextIndex[k] = j
            for i in range(k):
                if nextIndex[i] == j:
                    prefix = repeatCnt[i]
                    cur = (n1 - i) // (k - i) * (repeatCnt[k] - prefix)
                    suffix = repeatCnt[i + (n1 - i) % (k - i)] - prefix
                    return (prefix + cur + suffix) // n2

            k += 1
        return repeatCnt[-1]
