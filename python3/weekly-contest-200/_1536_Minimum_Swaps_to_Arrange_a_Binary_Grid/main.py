from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n, arr = len(grid), list()
        for row in grid:
            num = 0
            for elem in row[::-1] + [1]:
                if not elem:
                    num += 1
                else:
                    arr.append(num)
                    break

        res, i = 0, 0
        while i < n:
            if arr[i] < n - i - 1:
                j = i + 1
                while j < n and arr[j] < n - i - 1:
                    j += 1

                if j == n:
                    return -1

                arr = arr[:i] + [arr[j]] + arr[i: j] + arr[j + 1:]
                res += j - i
            i += 1
        return res
