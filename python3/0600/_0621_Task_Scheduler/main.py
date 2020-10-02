import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        hotPq, coolPq = list(), list()
        for cnt in counter.values():
            heapq.heappush(hotPq, [-cnt, -n - 1])

        t = 0
        while hotPq or coolPq:
            while coolPq and t - coolPq[0][0] > n:
                heapq.heappush(hotPq, heapq.heappop(coolPq)[::-1])
            if hotPq:
                cur = heapq.heappop(hotPq)
                cur[0] += 1
                cur[1] = t
                if cur[0] != 0:
                    heapq.heappush(coolPq, cur[::-1])
            t += 1
        return t

    # 1. Find the most frequent char, assume it's A with freq K
    # 2. Build K - 1 chunks, for each chunk it starts with A and n idle slots
    # 3. Append most frequent chars to the end, assume A, B are both most frequent, then append AB to the end.
    # 4. Find next frequent char to fill the idle slots sequentially
    # 5. Repeat this process util:
    #      5.1 there is no remaining tasks, then result will be total chunks length
    #      5.2 there is no remaining idle slots, then insert remaining tasks into end of each chunk sequentially,
    #      then result will be tasks length
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for t in tasks:
            cnt[ord(t) - ord('A')] += 1
        cnt.sort()

        i = 24
        while i >= 0 and cnt[i] == cnt[25]:
            i -= 1

        return max(len(tasks), (cnt[25] - 1) * (n + 1) + 25 - i)
