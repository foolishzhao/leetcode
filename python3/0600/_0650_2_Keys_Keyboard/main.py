class Solution:
    # Integer factorization
    # If the prime decomposition of n is n = p1^m1 * p2^m2 *...* pk^mk,
    # where each pi is a prime number, then the answer is p1*m1 + p2*m2 + ... + pk*mk
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(i // 2, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + i // j
                    break

        return dp[-1]
