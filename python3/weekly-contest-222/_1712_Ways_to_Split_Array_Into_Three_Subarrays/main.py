from typing import List
import bisect


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        s = prefix[-1]
        for i in range(1, n):
            l = prefix[i]
            if l * 3 > s:
                break

            j = bisect.bisect_left(prefix, l + l)
            k = bisect.bisect_right(prefix, (s + l) // 2)
            res += min(k, n) - max(j, i + 1)
        return res % (10 ** 9 + 7)
