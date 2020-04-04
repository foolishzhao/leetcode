class Solution:
    # consider negative number
    # corner case: "-0" to "0"
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = ""
        if (numerator ^ denominator) & (1 << 31):
            sign = "-"
        numerator, denominator = abs(numerator), abs(denominator)

        intPart = str(numerator // denominator)
        left = numerator % denominator

        if not left:
            return sign + intPart if intPart != "0" else intPart
        else:
            return sign + intPart + '.' + self.helper(left, denominator)

    def helper(self, numerator: int, denominator: int) -> str:
        li = []
        dt = {}
        i = 0
        while numerator:
            if numerator in dt:
                li.insert(dt[numerator], '(')
                li.append(')')
                return "".join(li)

            dt[numerator] = i
            i += 1

            numerator *= 10
            li.append(str(numerator // denominator))
            numerator %= denominator

        return "".join(li)
