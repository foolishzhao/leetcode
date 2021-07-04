class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def getNext(s):
            i = n - 1
            while s[i] <= s[i - 1]:
                i -= 1

            j = i + 1
            while j < n and s[j] > s[i - 1]:
                j += 1

            return s[:i - 1] + s[j - 1] + (s[i: j - 1] + s[i - 1] + s[j:])[::-1]

        cur, n, res = num, len(num), 0
        while k:
            k -= 1
            cur = getNext(cur)

        for i in range(n):
            if cur[i] != num[i]:
                j = i + 1
                while num[j] != cur[i]:
                    j += 1
                res += j - i
                num = num[:i] + num[j] + num[i: j] + num[j + 1:]
        return res
