class Solution:
    def generateTheString(self, n: int) -> str:
        res = ""
        for i in range(n - 1):
            res += 'a'

        res += 'a' if n % 2 == 1 else 'b'
        return res

    def generateTheString2(self, n: int) -> str:
        return 'a' * n if n % 2 == 1 else 'a' * (n - 1) + 'b'
