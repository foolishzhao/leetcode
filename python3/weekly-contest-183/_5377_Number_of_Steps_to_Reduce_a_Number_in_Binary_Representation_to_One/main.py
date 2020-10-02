class Solution:
    def numSteps(self, s: str) -> int:
        res, n = 0, int(s, 2)
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            else:
                n += 1
            res += 1
        return res

    def numSteps2(self, s: str) -> int:
        res, s = 0, list(s)
        while len(s) > 1:
            res += 1
            if s[-1] == '0':
                s.pop()
            else:
                found = False
                for i in range(len(s) - 1, -1, -1):
                    if s[i] == '0':
                        s[i] = '1'
                        found = True
                        break
                    else:
                        s[i] = '0'

                if not found:
                    s.insert(0, '1')
        return res
