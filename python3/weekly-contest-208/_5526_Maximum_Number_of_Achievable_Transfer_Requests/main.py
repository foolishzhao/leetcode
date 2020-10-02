from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def check(mask):
            edge, degree = 0, [0] * n
            for i in range(r):
                if mask & (1 << i):
                    edge += 1
                    degree[requests[i][0]] -= 1
                    degree[requests[i][1]] += 1
            return edge if not any(degree) else 0

        res, r = 0, len(requests)
        for m in range(1 << r):
            res = max(res, check(m))
        return res
