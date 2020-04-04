class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = 1
        if num < 0:
            sign = -1
            num = -num

        res = ""
        while num:
            res = str(num % 7) + res
            num //= 7

        if res == "":
            res = "0"
        return res if sign == 1 else "-" + res

    def convertToBase72(self, num: int) -> str:
        if num < 0:
            return '-' + self.convertToBase7(-num)

        if num < 7:
            return str(num)

        return self.convertToBase7(num // 7) + str(num % 7)
