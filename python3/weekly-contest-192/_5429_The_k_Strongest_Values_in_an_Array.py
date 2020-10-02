from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        m = sorted(arr)[(len(arr) - 1) // 2]
        arr = sorted([(abs(x - m), x) for x in arr])
        return [x[1] for x in arr[-k:]]
