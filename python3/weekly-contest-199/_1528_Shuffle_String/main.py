from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li = [None] * len(s)
        for i, idx in enumerate(indices):
            li[idx] = s[i]
        return ''.join(li)
