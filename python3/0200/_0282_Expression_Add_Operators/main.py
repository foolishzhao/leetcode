from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(expr, pos, cur, prev):
            if pos == n:
                if cur + prev == target:
                    res.append(expr)
                return

            for i in range(pos + 1, n + 1):
                if i > pos + 1 and num[pos] == '0':
                    break

                t = int(num[pos: i])
                if pos == 0:
                    dfs(expr + str(t), i, cur, t)
                else:
                    dfs(expr + '+' + str(t), i, cur + prev, t)
                    dfs(expr + '-' + str(t), i, cur + prev, -t)
                    dfs(expr + '*' + str(t), i, cur, prev * t)

        res, n = list(), len(num)
        dfs("", 0, 0, 0)
        return res
