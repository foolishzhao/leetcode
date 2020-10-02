from typing import List
import functools
import collections


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        @functools.lru_cache(None)
        def dp(t):
            if not t:
                return 0

            counter = [0] * 26
            for c in t:
                counter[ord(c) - ord('a')] += 1

            res = float('inf')
            for i in range(n):
                if t[0] in dt[i]:
                    subt = ""
                    for j, cnt in enumerate(counter):
                        char = chr(ord('a') + j)
                        cnt = max(0, cnt - dt[i].get(char, 0))
                        subt += char * cnt
                    subRes = dp(subt)
                    if subRes != -1:
                        res = min(res, subRes + 1)

            return -1 if res == float('inf') else res

        dt, n = list(), len(stickers)
        for sticker in stickers:
            dt.append(collections.Counter(sticker))
        return dp(''.join(sorted(target)))
