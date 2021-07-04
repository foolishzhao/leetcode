from typing import List
import collections


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()

        n, i, res = len(ages), 0, 0
        for j in range(1, n):
            while i < n and (ages[j] / 2 + 7) >= ages[i]:
                i += 1
            res += max(0, j - i)

        i = n - 1
        for j in range(n - 2, -1, -1):
            while i > j and ages[i] > ages[j]:
                i -= 1

            if ages[i] > 14:
                res += i - j

        return res

    def numFriendRequests2(self, ages: List[int]) -> int:
        def request(a, b):
            return a >= b > (a / 2 + 7)

        dt = collections.Counter(ages)
        return sum([request(x, y) * dt[x] * (dt[y] - (x == y)) for x in dt for y in dt])


if __name__ == '__main__':
    Solution().numFriendRequests2([16, 16])
