import collections
from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans =[]
        counter = collections.Counter(nums)
        d = counter.most_common()
        for i in range(k):
            ans.append(d[i][0])
        return ans



    def topKFrequent(self, nums, k):
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res

    class Solution:
        def topKFrequent(self, nums, k):
            res = []
            dic = Counter(nums)
            pq = list(list())
            for key, val in dic.items():
                if len(pq) >= k:
                    if val > pq[0][0]:
                        heapq.heappop(pq)
                        heapq.heappush(pq, [val, key])
                else:
                    heapq.heappush(pq, [val, key])
            for i in range(len(pq)):
                res.append(pq[i][1])
            return res

