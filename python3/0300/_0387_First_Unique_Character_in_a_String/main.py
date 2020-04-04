class Solution:
    def firstUniqChar(self, s: str) -> int:
        chrs = [0] * 26
        for c in s:
            chrs[ord(c) - ord('a')] += 1

        for i, c in enumerate(s):
            if chrs[ord(c) - ord('a')] == 1:
                return i

        return -1
