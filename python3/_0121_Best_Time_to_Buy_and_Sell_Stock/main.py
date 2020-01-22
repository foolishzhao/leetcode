from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        res, n = 0, len(prices)
        curMin = prices[0]
        for i in range(1, n):
            res = max(res, prices[i] - curMin)
            curMin = min(curMin, prices[i])

        return res

    # convert this to a max sub array problem
    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        res, n = 0, len(prices)
        curSum = 0
        for i in range(1, n):
            curSum = max(0, curSum + prices[i] - prices[i - 1])
            res = max(res, curSum)

        return res
