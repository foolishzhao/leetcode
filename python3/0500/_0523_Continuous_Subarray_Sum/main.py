from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = [0] * (n + 1)
        for i, num in enumerate(nums):
            s[i + 1] = s[i] + num

        for i in range(n - 1):
            for j in range(i + 2, n + 1):
                ss = s[j] - s[i]
                if not k and not ss:
                    return True
                if k and not (ss % k):
                    return True
        return False

    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        dt = {0: -1}
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            if k:
                cur %= k
            if cur in dt:
                if i - dt[cur] > 1:
                    return True
            else:
                # keep the oldest index
                dt[cur] = i
        return False
