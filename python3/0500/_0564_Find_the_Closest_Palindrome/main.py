class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n) <= 10:
            return str(int(n) - 1)

        l = len(n)
        if l % 2 == 0:
            half = n[:l >> 1]
            halfI = int(half)

            cs = [half + half[::-1]]
            if half == '1':
                cs.append('9')
            elif len(str(halfI - 1)) < len(half):
                cs.append(str(halfI - 1) + '9' + str(halfI - 1)[::-1])
            else:
                cs.append(str(halfI - 1) + str(halfI - 1)[::-1])

            if len(str(halfI + 1)) > len(half):
                cs.append(str(halfI + 1) + str(halfI + 1)[:-1][::-1])
            else:
                cs.append(str(halfI + 1) + str(halfI + 1)[::-1])
        else:
            half = n[:(l // 2 + 1)]
            halfI = int(half)
            cs = [half + half[:-1][::-1]]
            if len(str(halfI - 1)) < len(half):
                cs.append(str(halfI - 1) + str(halfI - 1)[::-1])
            else:
                cs.append(str(halfI - 1) + str(halfI - 1)[:-1][::-1])

            if len(str(halfI + 1)) > len(half):
                cs.append(str(halfI + 1) + str(halfI + 1)[:-2][::-1])
            else:
                cs.append(str(halfI + 1) + str(halfI + 1)[:-1][::-1])

        diff, res = float('inf'), ""
        for c in cs:
            if c != n:
                d = abs(int(c) - int(n))
                if d < diff or (d == diff and int(c) < int(res)):
                    diff, res = d, c
        return res

    # If answer has a different number of digits compared to input n, it must be of the form 999....999 or 1000...0001.
    # At most 5 candidates
    def nearestPalindromic2(self, n: str) -> str:
        l = len(n)
        cs = {str(10 ** (l - 1) - 1), str(10 ** l + 1)}
        half = int(n[:(l + 1) // 2])
        for d in [-1, 0, 1]:
            if l % 2 == 1:
                cs.add(str(half + d) + str(half + d)[:-1][::-1])
            else:
                cs.add(str(half + d) + str(half + d)[::-1])
        cs.discard(n)

        res, diff = "", float('inf')
        for c in cs:
            d = abs(int(c) - int(n))
            if d < diff or (d == diff and int(c) < int(res)):
                res, diff = c, d
        return res
