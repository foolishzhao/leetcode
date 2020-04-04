class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur, k = 1, k - 1
        while k > 0:
            steps = self.calcSteps(n, cur, cur + 1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10

        return cur

    def calcSteps(self, n, n1, n2):
        steps = 0
        while n1 <= n:
            steps += min(n + 1, n2) - n1
            n1 *= 10
            n2 *= 10

        return steps
