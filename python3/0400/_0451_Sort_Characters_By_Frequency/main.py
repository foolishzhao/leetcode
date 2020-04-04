import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = [0] * 128
        for c in s:
            cnt[ord(c)] += 1

        cntWithIdx = sorted([(i, c) for i, c in enumerate(cnt)], key=lambda x: -x[1])
        res = ""
        for i, c in cntWithIdx:
            res += chr(i) * c
        return res

    def frequencySort2(self, s: str) -> str:
        dt = collections.defaultdict(int)
        for c in s:
            dt[c] += 1

        items = sorted(dt.items(), key=lambda x: -x[1])
        res = ""
        for c, cnt in items:
            res += c * cnt
        return res
