from typing import List
import heapq


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n, pq = len(nums), list()
        for i in range(n - k + 1):
            heapq.heappush(pq, (nums[i], i))

        res, cur_idx, cur_i = list(), -1, n - k + 1
        while k:
            num, idx = heapq.heappop(pq)
            if idx > cur_idx:
                res.append(num)
                k -= 1
                cur_idx = idx

                if cur_i < n:
                    heapq.heappush(pq, (nums[cur_i], cur_i))
                    cur_i += 1
        return res

    def mostCompetitive2(self, nums: List[int], k: int) -> List[int]:
        st, n = list(), len(nums)
        for i, num in enumerate(nums):
            while st and st[-1] > num and len(st) - 1 + n - i >= k:
                st.pop()

            if len(st) < k:
                st.append(num)

        return st
