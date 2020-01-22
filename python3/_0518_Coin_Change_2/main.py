from typing import List


class Solution:
    """
    dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
        dp[i - 1][j]: means the number of combinations not using the ith coin
        dp[i][j - coins[i - 1]]: use at least one of the ith coin
    """

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[-1][-1]

    # optimize space based on solution 1
    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]

        return dp[-1]
