from typing import List
import heapq
import collections


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        pq = list()
        for word, count in counter.items():
            heapq.heappush(pq, Pair(word, count))
            if len(pq) > k:
                heapq.heappop(pq)

        return [p.word for p in sorted(pq, key=lambda x: (-x.freq, x.word))]
