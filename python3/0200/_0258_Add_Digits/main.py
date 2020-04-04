class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.getNext(num)

        return num

    def getNext(self, num) -> int:
        res = 0
        while num:
            res += num % 10
            num //= 10

        return res

    def addDigits2(self, num: int) -> int:
        while num >= 10:
            t = 0
            while num:
                t += num % 10
                num //= 10
            num = t

        return num

    def addDigits3(self, num: int) -> int:
        return 0 if not num else 1 + (num - 1) % 9
