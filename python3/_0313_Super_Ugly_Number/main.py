from typing import List


class Solution:
    # all the integer can be split into prime factor multiplication
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        idx = [0] * k

        res = [1]
        for _ in range(n - 1):
            t = [prime * res[idx[i]] for i, prime in enumerate(primes)]
            mt = min(t)
            res.append(mt)

            for i in range(k):
                if t[i] == mt:
                    idx[i] += 1

        return res[-1]


if __name__ == '__main__':
    Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])
