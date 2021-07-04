from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def dfs(curRes, num, p1, p2):
            nonlocal res
            if res or (p1[0] == '0' and len(p1) > 1) or (p2[0] == '0' and len(p2) > 1):
                return

            if int(p1) >= (1 << 31) or int(p2) >= (1 << 31):
                return

            if not num:
                curRes.append(p1)
                curRes.append(p2)
                res = curRes[:]
                return

            p3 = str(int(p1) + int(p2))
            if num.startswith(p3):
                curRes.append(p1)
                dfs(curRes, num[len(p3):], p2, p3)
                curRes.pop()

        n, res = len(num), list()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                dfs(list(), num[j + 1:], num[0: i + 1], num[i + 1:j + 1])
        return res
