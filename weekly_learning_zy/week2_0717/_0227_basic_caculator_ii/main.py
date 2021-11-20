class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        opWeight = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1
        }
        numSt, opSt, num = list(), list(), 0
        for c in s + '+':
            if c.isdigit()
                num

        numSt, opSt, num = list(), list(), 0
        for c in s + '+':
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
                        numSt.append(int(n1 / n2))
                opSt.append(c)

        return numSt.pop()