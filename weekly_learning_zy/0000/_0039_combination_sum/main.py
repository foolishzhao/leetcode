class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def dfs(curTarget, curRes):
            if curTarget == 0:
                res.append(curRes)
                return
            for c in candidates:
                if c > curTarget: break
                if curRes and c < curRes[-1]:
                    continue
                else:
                    dfs(curTarget - c, curRes + [c])

        dfs(target, [])
        return res





