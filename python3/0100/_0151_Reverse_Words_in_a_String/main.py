class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        if not s:
            return s

        sArr = s.split()
        sArr.reverse()

        return " ".join(sArr)
