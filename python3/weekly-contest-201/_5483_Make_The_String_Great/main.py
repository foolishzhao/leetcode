class Solution:
    def makeGood(self, s: str) -> str:
        li = list()
        for c in s:
            if not li or abs(ord(li[-1]) - ord(c)) != 32:
                li.append(c)
            else:
                li.pop()
        return ''.join(li)
