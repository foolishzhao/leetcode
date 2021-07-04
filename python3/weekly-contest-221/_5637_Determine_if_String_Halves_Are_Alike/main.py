class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = set('aeiouAEIOU')
        n, l, r = len(s) // 2, 0, 0
        for i in range(n):
            if s[i] in vowel:
                l += 1
            if s[-i - 1] in vowel:
                r += 1
        return l == r
