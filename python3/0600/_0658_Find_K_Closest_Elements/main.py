from typing import List
import heapq


class Solution:
    # O(n) time complexity, O(k) space complexity
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = list()
        for y in arr:
            heapq.heappush(q, (-abs(x - y), -y))
            if len(q) > k:
                heapq.heappop(q)
        return sorted([-v[1] for v in q])

    # O(n - k) time complexity, O(1) space complexity
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if x - arr[l] > arr[r] - x:
                l += 1
            else:
                r -= 1
        return arr[l: r + 1]

    # O(log(n - k)) time complexity, O(1) space complexity
    # Assume A[mid] ~ A[mid + k] is sliding window
    # case 1: x - A[mid] < A[mid + k] - x, need to move window go left
    # -------x----A[mid]-----------------A[mid + k]----------
    # case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
    # -------A[mid]----x-----------------A[mid + k]----------
    # case 3: x - A[mid] > A[mid + k] - x, need to move window go right
    # -------A[mid]------------------x---A[mid + k]----------
    # case 4: x - A[mid] > A[mid + k] - x, need to move window go right
    # -------A[mid]---------------------A[mid + k]----x------
    def findClosestElements3(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        # search start pos of k consecutive elements
        while lo < hi:
            m = (lo + hi) // 2
            # compare start of m and end of m + 1
            if x - arr[m] > arr[m + k] - x:  # m + 1 is better than m, m - 1, ...
                lo = m + 1
            else:  # m is better than m + 1, m + 2, ...
                hi = m
        return arr[lo: lo + k]
