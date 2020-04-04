class Solution:
    def myAtoi(self, str: str) -> int:
        res, sign, n, i = 0, 1, len(str), 0

        while i < n and str[i] == ' ':
            i += 1

        if i < n and (str[i] == '+' or str[i] == '-'):
            if str[i] == '-':
                sign = -1
            i += 1

        while i < n:
            c = str[i]
            if '0' <= c <= '9':
                res = res * 10 + int(c)

                if sign * res < -(1 << 31):
                    return -(1 << 31)
                elif sign * res >= (1 << 31):
                    return (1 << 31) - 1
            else:
                break
            i += 1

        return sign * res
