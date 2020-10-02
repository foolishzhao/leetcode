from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res, i = 0, 0
        negCnt, first, last = 0, -1, -1
        for j, v in enumerate(nums + [0]):
            if v < 0:
                negCnt += 1
                if first == -1:
                    first = j
                last = j
            elif v == 0:
                if negCnt % 2 == 0:
                    res = max(res, j - i)
                else:
                    res = max(res, last - i, j - first - 1)
                i = j + 1
                negCnt, first, last = 0, -1, -1

        return res

    # pos[i]: max len of positive product ends with nums[i - 1]
    # neg[i]: max len of negative product ends with nums[i - 1]
    def getMaxLen2(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = [0] * (n + 1), [0] * (n + 1)
        for i, v in enumerate(nums):
            if v > 0:
                pos[i + 1] = pos[i] + 1
                if neg[i]:
                    neg[i + 1] = neg[i] + 1
            elif v < 0:
                if neg[i]:
                    pos[i + 1] = neg[i] + 1
                neg[i + 1] = pos[i] + 1
        return max(pos)
