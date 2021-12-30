import collections
import heapq
from typing import List


class Solution:
    #时间复杂度太高了 跑不过
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq =[]
        ans = []
        for i in range(len(nums) -k +1):
            t = i
            while  t < i + k :
                heapq.heappush(pq, nums[t])
                t += 1
            for _ in range(k-1):
                heapq.heappop(pq)
            ans.append(heapq.heappop(pq))
        return ans

    def maxSlidingWindow2(self, nums, k):
        res = []
        deque = list()
        for i, v in enumerate(nums):
            while deque and v >= deque[-1][1]:
                deque.pop()
            deque.append((i, v))
            print(deque)

            if i >= k and deque[0][0] == i - k:
                print("---here---")
                deque.pop(0)

            if i >= k - 1:
                res.append(deque[0][1])
                print("---res--- : " ,res)
        return res

    def maxSlidingWindow3(self, nums, k):
        res = []
        dq = collections.deque()
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] <= n:
                dq.pop()
            dq += [i]
            print(dq)

            # make sure the leftmost one is in-bound
            if i - dq[0] >= k:
                dq.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            #if i + 1 >= k:
            res.append(nums[dq[0]])
        return res

if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    ans = Solution().maxSlidingWindow2(nums, k)
    print(ans)