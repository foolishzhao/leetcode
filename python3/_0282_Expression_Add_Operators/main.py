from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.dfs(res, "", num, 0, target, 0, 0)
        return res

    def dfs(self, res, curRes, num, pos, target, cur, prev):
        if pos == len(num):
            if cur + prev == target:
                res.append(curRes)
            return

        n = len(num)
        for i in range(pos + 1, n + 1):
            if i > pos + 1 and num[pos] == '0':
                break

            t = int(num[pos:i])
            if pos == 0:
                self.dfs(res, curRes + str(t), num, i, target, 0, t)
            else:
                self.dfs(res, curRes + '+' + str(t), num, i, target, cur + prev, t)
                self.dfs(res, curRes + '-' + str(t), num, i, target, cur + prev, -t)
                self.dfs(res, curRes + '*' + str(t), num, i, target, cur, prev * t)
