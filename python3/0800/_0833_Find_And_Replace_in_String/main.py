from typing import List


class Solution:
    def findReplaceString(self, s: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        s = list(s)
        x = sorted([(idx, src, tar) for idx, src, tar in zip(indexes, sources, targets)])

        for idx, src, tar in x[::-1]:
            if ''.join(s[idx: idx + len(src)]) == src:
                s[idx: idx + len(src)] = list(tar)

        return ''.join(s)
