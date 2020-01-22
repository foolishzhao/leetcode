class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

        res, i = "", 0
        while num > 0:
            while num >= mappings[i][0]:
                res += mappings[i][1]
                num -= mappings[i][0]
            i += 1

        return res

    def intToRoman2(self, num: int) -> str:
        t = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"],
        ]

        return t[3][num // 1000] + t[2][num % 1000 // 100] + t[1][num % 100 // 10] + t[0][num % 10]
