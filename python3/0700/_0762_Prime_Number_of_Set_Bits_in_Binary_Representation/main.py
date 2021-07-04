import math


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def isPrime(x):
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        def setBits(x):
            return bin(x).count('1')

        primeSet = {i for i in range(2, 32) if isPrime(i)}
        return sum([1 for i in range(L, R + 1) if setBits(i) in primeSet])
