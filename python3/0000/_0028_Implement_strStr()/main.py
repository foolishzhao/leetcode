from typing import List


class Solution:
    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        hLen, nLen = len(haystack), len(needle)
        for i in range(hLen - nLen + 1):
            j = 0
            while j < nLen:
                if haystack[i + j] != needle[j]:
                    break
                j += 1

            if j == nLen:
                return i

        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        hLen, nLen = len(haystack), len(needle)
        if hLen >= nLen:
            nxt = self.getNext(needle)
            i, j = 0, 0
            while i < hLen:
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                    if j == nLen:
                        return i - nLen
                elif j > 0:
                    j = nxt[j]
                else:
                    i += 1

        return -1

    def getNext(self, s: str) -> List[int]:
        i, j, n = 0, 1, len(s)
        res = [0] * (n + 1)
        while j < n:
            if s[i] == s[j]:
                i += 1
                j += 1
                res[j] = i
            elif i > 0:
                i = res[i]
            else:
                j += 1

        return res


if __name__ == '__main__':
    Solution().strStr("aaa", "aaa")
