class Solution:
    def toHex(self, num: int) -> str:
        res = ""
        for i in range(7, -1, -1):
            res += self.helper((num >> (i * 4)) & 0xf)

        res = res.lstrip('0')
        return '0' if not res else res

    def helper(self, num):
        if num < 10:
            return str(num)
        return chr(ord('a') + num - 10)

    def toHex2(self, num: int) -> str:
        dt = "0123456789abcdef"

        res = ""
        for _ in range(8):
            res = dt[num & 15] + res
            num >>= 4

        res = res.lstrip('0')
        return '0' if not res else res
