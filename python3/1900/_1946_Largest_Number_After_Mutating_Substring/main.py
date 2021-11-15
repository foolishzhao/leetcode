from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num, i, n = list(num), 0, len(num)
        while i < n:
            if num[i] < str(change[int(num[i])]):
                break
            i += 1

        j = i
        while j < n:
            if num[j] > str(change[int(num[j])]):
                break
            num[j] = str(change[int(num[j])])
            j += 1

        return ''.join(num)
