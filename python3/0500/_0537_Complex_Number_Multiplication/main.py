class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def parse(t):
            x, y = t.split('+')
            return int(x), int(y[:-1])

        x1, y1 = parse(a)
        x2, y2 = parse(b)
        return str(x1 * x2 - y1 * y2) + '+' + str(x1 * y2 + x2 * y1) + "i"
