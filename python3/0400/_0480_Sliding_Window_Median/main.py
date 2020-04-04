from typing import List
import bisect
import heapq


class Solution:
    # Time complexity: O(n*k), space complexity: O(k)
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = list()

        window, m = list(), k // 2
        for i, num in enumerate(nums):
            bisect.insort(window, num)
            if i >= k - 1:
                res.append(window[m] if k % 2 == 1 else (window[m - 1] + window[m]) / 2)
                window.remove(nums[i - k + 1])

        return res

    # Time complexity: O(n*log(n)), space complexity: O(n)
    def medianSlidingWindow2(self, nums: List[int], k: int) -> List[float]:
        res, lo, hi = list(), list(), list()
        for i, num in enumerate(nums[:k]):
            if len(lo) == len(hi):
                # use negative index to let same num in index order
                x, y = heapq.heappushpop(lo, (-num, -i))
                heapq.heappush(hi, (-x, -y))
            else:
                x, y = heapq.heappushpop(hi, (num, i))
                heapq.heappush(lo, (-x, -y))

        res.append(hi[0][0] if k % 2 == 1 else (hi[0][0] - lo[0][0]) / 2)
        # note enumerate's param needs to start from k
        for i, num in enumerate(nums[k:], k):
            x, y = heapq.heappushpop(hi, (num, i))
            heapq.heappush(lo, (-x, -y))

            # lo and hi are balanced for latest k nums already
            # if this should be out num is in hi, we should add new num to hi, else add new num to lo
            if nums[i - k] > -lo[0][0]:
                x, y = heapq.heappop(lo)
                heapq.heappush(hi, (-x, -y))

            while lo and -lo[0][1] <= i - k:
                heapq.heappop(lo)

            while hi and hi[0][1] <= i - k:
                heapq.heappop(hi)

            res.append(hi[0][0] if k % 2 == 1 else (hi[0][0] - lo[0][0]) / 2)

        return res


if __name__ == '__main__':
    Solution().medianSlidingWindow2([4, 1, 7, 1, 8, 7, 8, 7, 7, 4], 4)
