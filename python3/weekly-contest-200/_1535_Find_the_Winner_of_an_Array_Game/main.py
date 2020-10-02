from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur, win = arr[0], 0
        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                win = 1
            else:
                win += 1
            if win == k:
                return cur
        return cur
