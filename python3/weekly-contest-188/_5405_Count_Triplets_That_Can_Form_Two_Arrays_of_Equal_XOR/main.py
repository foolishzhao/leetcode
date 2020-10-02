from typing import List
import collections


class Solution:
    # O(N^3), O(N)
    def countTriplets(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        xor = [0] * (n + 1)
        for i, v in enumerate(arr):
            xor[i + 1] = xor[i] ^ v

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a = xor[i] ^ xor[j]
                    b = xor[k + 1] ^ xor[j]
                    res += a == b
        return res

    # O(N^2), O(N)
    def countTriplets2(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        xor = [0] * (n + 1)
        for i, v in enumerate(arr):
            xor[i + 1] = xor[i] ^ v

        for i in range(n):
            for k in range(i + 1, n):
                if xor[k + 1] == xor[i]:
                    res += k - i
        return res

    # O(N^2), O(1)
    def countTriplets3(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        res, n = 0, len(arr)
        for i in range(1, n):
            for k in range(i + 1, n):
                if arr[k] == arr[i - 1]:
                    res += k - i
        return res

    # O(N), O(N)
    def countTriplets4(self, arr: List[int]) -> int:
        dt = collections.defaultdict(list)
        dt[0].append(0)

        arr.insert(0, 0)
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
            dt[arr[i]].append(i)

        res, n = 0, len(arr)
        for k in range(2, n):
            for i in dt[arr[k]]:
                if i < k:
                    res += k - i - 1
        return res
