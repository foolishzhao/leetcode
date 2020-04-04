class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)

        num1 = [int(x) for x in list(num1)[::-1]]
        num2 = [int(x) for x in list(num2)[::-1]]
        for i, v in enumerate(num2):
            num1[i] += v

        c = 0
        for i, v in enumerate(num1):
            cur = v + c
            num1[i] = cur % 10
            c = cur // 10

        if c:
            num1.append(c)

        return "".join([str(x) for x in num1][::-1])
