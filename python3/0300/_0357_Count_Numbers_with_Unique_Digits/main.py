class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1

        res, cur, avail = 10, 9, 9
        while n > 1 and avail:
            cur *= avail
            res += cur

            avail -= 1
            n -= 1

        return res

    # backtracking
    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        return self.getCount(min(n, 10), 0, [False] * 10)

    def getCount(self, n, idx, visited):
        if idx == n:
            return 1

        count = 1
        i = 1 if not idx else 0
        while i <= 9:
            if not visited[i]:
                visited[i] = True
                count += self.getCount(n, idx + 1, visited)
                visited[i] = False
            i += 1

        return count
