from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(i):
            res = dt[i].importance
            for s in dt[i].subordinates:
                res += dfs(s)
            return res

        dt = {e.id: e for e in employees}
        return dfs(id)
