from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.res, worker = float('inf'), [0] * k
        jobs.sort(reverse=True)

        def dfs(curIdx, kStart):
            if curIdx == len(jobs):
                self.res = min(self.res, max(worker))
                return

            seen = set()
            for i in range(kStart, kStart + k):
                j = i % k
                if worker[j] in seen:
                    continue

                if worker[j] + jobs[curIdx] >= self.res:
                    continue

                seen.add(worker[j])
                worker[j] += jobs[curIdx]
                dfs(curIdx + 1, kStart + 1)
                worker[j] -= jobs[curIdx]

        dfs(0, 0)
        return self.res
