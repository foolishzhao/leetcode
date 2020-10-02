from typing import List


class Solution:
    # buy[i] represents max profit at day i given the last action is a buy action
    # sell[i] represents max profit at day i given the last action is a sell action
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy, sell = [0] * n, [0] * n

        buy[0] = -prices[0]
        for i in range(1, n):
            # last buy action happen before day i, or in day i
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            # last sell action happen before day i, or in day i
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)
        return sell[-1]


if __name__ == '__main__':
    Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
