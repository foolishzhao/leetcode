from typing import List


class Solution:
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curCan, curRes, curTar):
            if curTar == 0:
                res.append(curRes)
                return
            for i, c in enumerate(curCan):
                if i > 0 and c == curCan[i - 1]:
                    continue
                if c > curTar:
                    break
                dfs(curCan[i + 1:], curRes + [c], curTar - c)

        dfs(sorted(candidates), [], target)
        return res
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        def dfs(curCan, curRes, curTar):
            if curTar == 0:
                res.append(curRes)
                return
            for i in range(len(curCan)):
                if i >0 and curCan[i] == curCan[i-1]:
                    continue
                if curCan[i] > curTar:
                    break
                dfs(curCan[i+1:], curRes + [curCan[i]], curTar - curCan[i])

        res = []
        dfs(sorted(candidates), [], target)
        return res




if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    ans = Solution().combinationSum2(candidates,target)
    print("--------", ans)
