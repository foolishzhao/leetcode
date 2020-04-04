class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, i, j, n, maxCnt = 0, 0, 0, len(s), 0
        count = [0] * 26
        while j < n:
            idx = ord(s[j]) - ord('A')
            count[idx] += 1

            maxCnt = max(maxCnt, count[idx])

            while j - i + 1 - maxCnt > k:
                count[ord(s[i]) - ord('A')] -= 1
                i += 1
                maxCnt = max(count)

            res = max(res, j - i + 1)
            j += 1

        return res
