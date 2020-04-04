from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = list()
        self.dfs(res, num, 0, 9)
        return res

    def dfs(self, res, n, cur, curPos):
        if n == 0:
            h, m = cur >> 6, cur & 0b111111
            if h <= 11 and m <= 59:
                if m < 10:
                    res.append(str(h) + ":0" + str(m))
                else:
                    res.append(str(h) + ":" + str(m))

            return

        if curPos >= 0:
            self.dfs(res, n, cur, curPos - 1)
            self.dfs(res, n - 1, cur | (1 << curPos), curPos - 1)

    def readBinaryWatch2(self, num: int) -> List[str]:
        def numOfBitOne(n):
            res = 0
            for i in range(10):
                if n & (1 << i):
                    res += 1
            return res

        res = list()
        for h in range(12):
            for m in range(60):
                if numOfBitOne(h) + numOfBitOne(m) == num:
                    if m < 10:
                        res.append(str(h) + ":0" + str(m))
                    else:
                        res.append(str(h) + ":" + str(m))
        return res


if __name__ == '__main__':
    Solution().readBinaryWatch(1)
