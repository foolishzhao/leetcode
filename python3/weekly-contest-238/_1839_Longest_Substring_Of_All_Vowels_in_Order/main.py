class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res, i, seen = 0, 0, set()
        for j, c in enumerate(word):
            if j and c < word[j - 1]:
                seen = set()
                i = j
            seen.add(c)
            if len(seen) == 5:
                res = max(res, j - i + 1)
        return res
