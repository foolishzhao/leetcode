import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt, n = [0] * 26, len(S)
        for c in S:
            idx = ord(c) - ord('a')
            cnt[idx] += 1

        if max(cnt) > (n + 1) // 2:
            return ""

        pq = list()
        for i, c in enumerate(cnt):
            if c:
                heapq.heappush(pq, (-c, chr(ord('a') + i)))

        res, prevCnt, prevC = '', 0, ''
        while pq:
            cnt, c = heapq.heappop(pq)
            res += c
            if prevCnt < 0:
                heapq.heappush(pq, (prevCnt, prevC))

            cnt += 1
            prevCnt, prevC = cnt, c
        return res
