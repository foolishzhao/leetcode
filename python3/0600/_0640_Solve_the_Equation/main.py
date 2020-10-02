class Solution:
    def solveEquation(self, equation: str) -> str:
        if not equation:
            return "No solution"
        equation = equation.replace("-", "+-")
        parts = equation.split("=")
        x1, y1 = self.parse(parts[0])
        x2, y2 = self.parse(parts[1])
        x3, y3 = x1 - x2, y2 - y1
        if not x3 and not y3:
            return "Infinite solutions"
        if not x3:
            return "No solution"
        return "x=" + str(y3 // x3)

    def parse(self, part):
        a, b = 0, 0
        for x in part.split("+"):
            if x:
                if x[-1] == 'x':
                    x = x[:-1]
                    if not x:
                        a += 1
                    elif x == '-':
                        a -= 1
                    else:
                        a += int(x)
                else:
                    b += int(x)
        return a, b
