class Solution:
    def __init__(self):
        self.p2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.p3 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                   "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    def blowThousand(self, num):
        res = []
        if num >= 100:
            res.append(self.p3[num // 100 - 1])
            res.append("Hundred")
            num %= 100

        if num >= 20:
            res.append(self.p2[num // 10 - 2])
            num %= 10

        if num >= 1:
            res.append(self.p3[num - 1])

        return res

    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        res = []
        if num >= 10 ** 9:
            res.extend(self.blowThousand(num // (10 ** 9)))
            res.append("Billion")
            num %= 10 ** 9

        if num >= 10 ** 6:
            res.extend(self.blowThousand(num // (10 ** 6)))
            res.append("Million")
            num %= 10 ** 6

        if num >= 10 ** 3:
            res.extend(self.blowThousand(num // (10 ** 3)))
            res.append("Thousand")
            num %= 10 ** 3

        res.extend(self.blowThousand(num))

        return " ".join(res)
