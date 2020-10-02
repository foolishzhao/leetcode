from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for x in arr:
            cnt[x % k] += 1

        i, j = 1, k - 1
        while i < j:
            if cnt[i] != cnt[j]:
                return False
            i += 1
            j -= 1

        return not cnt[i] % 2 if i == j else True
