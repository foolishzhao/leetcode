class Solution:
    # recursive
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(1, n):
                if max(i, j) > n - i - j:
                    break

                if self.dfs(num[:i], num[i: i + j], num[i + j:]):
                    return True

        return False

    def dfs(self, prev, cur, num) -> bool:
        if not num:
            return True

        if prev[0] == '0' and len(prev) > 1:
            return False

        if cur[0] == '0' and len(cur) > 1:
            return False

        nxt = str(int(prev) + int(cur))
        return num.startswith(nxt) and self.dfs(cur, nxt, num[len(nxt):])

    # iterate
    def isAdditiveNumber2(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n // 2 + 1):
            for j in range(1, n):
                if max(i, j) > n - i - j:
                    break

                if self.helper(num[:i], num[i: i + j], num[i + j:]):
                    return True

        return False

    def helper(self, prev, cur, num) -> bool:
        while num:
            if prev[0] == '0' and len(prev) > 1:
                return False

            if cur[0] == '0' and len(cur) > 1:
                return False

            nxt = str(int(prev) + int(cur))
            if num.startswith(nxt):
                prev, cur, num = cur, nxt, num[len(nxt):]
            else:
                return False

        return True


if __name__ == '__main__':
    Solution().isAdditiveNumber("199100199")
