from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        left, right = [0] * n, [0] * n
        leftMin, rightMax = prices[0], prices[-1]

        for i in range(1, n):
            left[i] = max(left[i - 1], prices[i] - leftMin)
            leftMin = min(leftMin, prices[i])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], rightMax - prices[i])
            rightMax = max(rightMax, prices[i])

        return max([x + y for x, y in zip(left, right)])


if __name__ == '__main__':
    Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
