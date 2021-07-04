from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def isValid(x):
            if x == "0":
                return True

            if x[0] == '0' and x[1] != '.':
                return False

            if x[-1] == '0' and '.' in x:
                return False

            return True

        def getCan(x):
            can = [x]
            for i in range(1, len(x)):
                can.append(x[:i] + "." + x[i:])
            return [y for y in can if isValid(y)]

        res, s = list(), s[1:-1]
        for i in range(1, len(s)):
            lc, rc = getCan(s[0:i]), getCan(s[i:])
            for l in lc:
                for r in rc:
                    res.append('(' + l + ', ' + r + ')')
        return res
