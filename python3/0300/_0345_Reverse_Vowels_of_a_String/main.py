class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            return c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        # convert str to char list
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not isVowel(s[i]):
                i += 1
            while i < j and not isVowel(s[j]):
                j -= 1

            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)
