class Solution:
    def reformat(self, s: str) -> str:
        letters, digits = list(), list()
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                letters.append(c)

        if abs(len(letters) - len(digits)) > 1:
            return ""

        if len(digits) > len(letters):
            letters, digits = digits, letters

        res = ""
        for i in range(len(digits)):
            res += letters[i] + digits[i]
        if len(letters) > len(digits):
            res += letters[-1]
        return res
