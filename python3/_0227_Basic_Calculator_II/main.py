class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        opWeight = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1,
        }
        numSt, opSt = list(), list()
        num = 0
        for c in s + "+":
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in opWeight:
                numSt.append(num)
                num = 0
                while opSt and opWeight[opSt[-1]] >= opWeight[c]:
                    n2, n1 = numSt.pop(), numSt.pop()
                    op = opSt.pop()
                    if op == '+':
                        numSt.append(n1 + n2)
                    elif op == '-':
                        numSt.append(n1 - n2)
                    elif op == '*':
                        numSt.append(n1 * n2)
                    else:
                        numSt.append(n1 // n2)
                opSt.append(c)

        return numSt.pop()

    def calculate2(self, s: str) -> int:
        # one + for last sign, one + for last calculation
        s = s.replace(" ", "") + "++"

        res, prev, sign = 0, 0, '+'
        i, n = 0, len(s)
        while i < n:
            cur = 0
            while s[i].isdigit():
                cur = cur * 10 + int(s[i])
                i += 1

            if sign == '+':
                res += prev
                prev = cur
            elif sign == '-':
                res += prev
                prev = -cur
            elif sign == '*':
                prev *= cur
            else:
                # can't use prev // cur, if prev < 0, // will truncate towards negative, we want truncate towards zero
                prev = int(prev / cur)

            sign = s[i]
            i += 1

        return res


if __name__ == '__main__':
    Solution().calculate2("14-3/2")
