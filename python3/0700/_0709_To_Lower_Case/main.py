class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for c in str:
            if 'A' <= c <= 'Z':
                res += chr(ord(c) - ord('A') + ord('a'))
            else:
                res += c
        return res
