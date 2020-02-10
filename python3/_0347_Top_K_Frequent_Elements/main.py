from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = collections.defaultdict(int)
        for num in nums:
            dt[num] += 1

        pq = list()
        for num, freq in dt.items():
            if len(pq) < k:
                heapq.heappush(pq, (freq, num))
            elif pq[0][0] < freq:
                heapq.heappop(pq)
                heapq.heappush(pq, (freq, num))

        return [num for _, num in pq]

    # bucket sort
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        dt = collections.defaultdict(int)
        for num in nums:
            dt[num] += 1

        # [[]] * n is wrong
        bucket = [None] * (len(nums) + 1)
        for num, freq in dt.items():
            if not bucket[freq]:
                bucket[freq] = list()
            bucket[freq].append(num)

        res = list()
        for nums in bucket[::-1]:
            if len(res) == k:
                break

            if not nums:
                continue

            if len(res) + len(nums) <= k:
                res.extend(nums)
            else:
                res.extend(nums[:k - len(res)])

        return res


if __name__ == '__main__':
    Solution().topKFrequent2([3, 0, 1, 0], 1)
