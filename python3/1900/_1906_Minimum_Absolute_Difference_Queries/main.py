from typing import List
import bisect


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        bucket = [list() for _ in range(100)]
        for i, num in enumerate(nums):
            bucket[num - 1].append(i)

        res = list()
        for ql, qr in queries:
            curRes, prev = float('inf'), None
            for b in range(100):
                lIdx = bisect.bisect_left(bucket[b], ql)
                if lIdx == len(bucket[b]):
                    continue

                if bucket[b][lIdx] <= qr:
                    if prev is not None:
                        curRes = min(curRes, b - prev)
                    prev = b
            res.append(-1 if curRes == float('inf') else curRes)
        return res

    def minDifference2(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        prefix, cnt = [[0] * 100 for _ in range(n + 1)], [0] * 100

        for i in range(n):
            cnt[nums[i] - 1] += 1
            for j in range(100):
                prefix[i + 1][j] = cnt[j]

        res = list()
        for ql, qr in queries:
            cnt = [0] * 100
            for j in range(100):
                cnt[j] = prefix[qr + 1][j] - prefix[ql][j]

            curRes, prev = float('inf'), None
            for j in range(100):
                if cnt[j]:
                    if prev is not None:
                        curRes = min(curRes, j - prev)
                    prev = j
            res.append(-1 if curRes == float('inf') else curRes)
        return res
