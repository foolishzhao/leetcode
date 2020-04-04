import math


class Solution:
    """
        k ^ m + k ^ (m - 1) + ... + 1 = n (1)
        n - 1 = k(k ^ (m - 1) + ... + 1)
        n - 1 = k(n - k ^ m)
        k ^ (m + 1) = kn - n + 1
        (k ^ (m + 1) - 1) / k - 1 = n

        from (1) k ^ m < n
        for m > 1,  n = k ^ m + k ^ (m - 1) + ... + 1  < (k + 1) ^ m
        k ^ m < n < (k + 1) ^ m  ->  k = math.floor(n ** (m ** -1))

        k >= 2 -> math.floor(n ** (m ** -1)) >= 2 -> m ** -1 >= logn2 -> m <= log2n

        1 < m <= log2n
    """

    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for m in range(int(math.log2(n)), 1, -1):
            k = int(n ** (m ** -1))
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)

        return str(n - 1)

    # (k ^ (m + 1) - 1) / k - 1 = n
    def smallestGoodBase2(self, n: str) -> str:
        n = int(n)
        for m in range(int(math.log2(n)), 0, -1):
            left, right = 2, n - 1
            while left <= right:
                k = (right - left) // 2 + left
                if k ** (m + 1) - 1 == (k - 1) * n:
                    return str(k)
                elif k ** (m + 1) - 1 > (k - 1) * n:
                    right = k - 1
                else:
                    left = k + 1


if __name__ == '__main__':
    Solution().smallestGoodBase2("13")
