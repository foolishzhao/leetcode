from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def canEarn(subarr):
            n = len(subarr)
            dp = [0] * (n + 1)
            dp[0] = 0
            dp[1] = subarr[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 2] + subarr[i - 1], dp[i - 1])
            return dp[-1]

        points = [0] * 10001
        for num in nums:
            points[num] += num

        res, i, n = 0, 0, len(points)
        while i < n:
            while i < n and not points[i]:
                i += 1

            if i == n:
                break

            j = i + 1
            while j < n and points[j]:
                j += 1

            res += canEarn(points[i: j])
            i = j

        return res

    def deleteAndEarn2(self, nums: List[int]) -> int:
        points = [0] * 10001
        for num in nums:
            points[num] += num

        prev, cur = 0, 0
        for point in points:
            prev, cur = cur, max(prev + point, cur)
        return cur
