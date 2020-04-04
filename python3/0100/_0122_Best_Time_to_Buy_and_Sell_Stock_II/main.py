from typing import List


class Solution:
    # suppose the monotone sequence  "e1 <= ... <= en", the profit is "en - e1 = (e2 - e1) + ..."
    # suppose another one is "e1 <= ... >= ei <=... <= en", the profit is "(ei-1 - e1) + (en- ei)".
    # So just target at monotone sequences.
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        res, n = 0, len(prices)
        for i in range(1, n):
            res += max(0, prices[i] - prices[i - 1])

        return res
