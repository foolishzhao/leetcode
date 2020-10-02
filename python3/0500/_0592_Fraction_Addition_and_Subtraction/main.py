import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        exprs = [x for x in expression.replace('-', '+-').split('+') if x]
        res = exprs[0]
        for expr in exprs[1:]:
            res = self.add(res, expr)
        return self.reduce(res)

    def add(self, e1, e2):
        x1, y1 = [int(x) for x in e1.split("/")]
        x2, y2 = [int(x) for x in e2.split("/")]
        return str(x1 * y2 + x2 * y1) + '/' + str(y1 * y2)

    def reduce(self, e):
        parts = [int(x) for x in e.split("/")]
        g = math.gcd(parts[0], parts[1])
        return "/".join([str(x // g) for x in parts])
