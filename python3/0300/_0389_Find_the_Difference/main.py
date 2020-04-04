class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        chrs = [0] * 26
        for c in t:
            chrs[ord(c) - ord('a')] += 1

        for c in s:
            chrs[ord(c) - ord('a')] -= 1

        for i in range(26):
            if chrs[i] == 1:
                return chr(ord('a') + i)
