from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        res = [None] * len(nums)
        for i, p in enumerate(sorted(enumerate(nums), key=lambda x: -x[1])):
            if i == 0:
                res[p[0]] = "Gold Medal"
            elif i == 1:
                res[p[0]] = "Silver Medal"
            elif i == 2:
                res[p[0]] = "Bronze Medal"
            else:
                res[p[0]] = str(i + 1)
        return res
