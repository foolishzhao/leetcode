class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(x):
            return x == x[::-1]

        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1

        return i >= j or isPalindrome(s[i + 1: j + 1]) or isPalindrome(s[i: j])
