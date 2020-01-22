from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # canBuy[i] means maxProfit with the i-th state of can buy
        canBuy, canSell, coolDown = [0] * n, [0] * n, [0] * n

        canSell[0] = -prices[0]
        for i in range(1, n):
            # stay at canBuy, or rest from coolDown
            canBuy[i] = max(canBuy[i - 1], coolDown[i - 1])
            # stay at canSell, or buy from canBuy
            canSell[i] = max(canSell[i - 1], canBuy[i - 1] - prices[i])
            # sell from canSell
            coolDown[i] = canSell[i - 1] + prices[i]

        return max(canBuy[-1], coolDown[-1])

    # optimize space
    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        canBuy, canSell, coolDown = 0, -prices[0], 0
        for i in range(1, n):
            prevCanSell = canSell
            canSell = max(canSell, canBuy - prices[i])
            canBuy = max(canBuy, coolDown)
            coolDown = prevCanSell + prices[i]

        return max(canBuy, coolDown)
