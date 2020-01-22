from queue import PriorityQueue
from typing import List


class Solution:
    # time complexity: O(n)
    # space complexity: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k > len(nums):
            return 0

        # default min heap
        pq = PriorityQueue()
        for num in nums:
            if pq.qsize() < k:
                pq.put(num)
            else:
                pq.put(max(pq.get(), num))

        return pq.get()

    # time complexity: O(n)
    # space complexity: O(1)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        if not nums or not k or k > len(nums):
            return 0

        return self.helper(nums, 0, len(nums) - 1, k)

    # kth largest, so need to sort desc
    def helper(self, nums: List[int], left: int, right: int, k: int) -> int:
        pivot = nums[right]
        i, j = left, left
        while j < right:
            if nums[j] > pivot:
                if i == j:
                    i += 1
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            else:
                j += 1
        nums[i], nums[right] = nums[right], nums[i]

        if i - left + 1 == k:
            return nums[i]
        elif i - left + 1 > k:
            return self.helper(nums, left, i - 1, k)
        else:
            return self.helper(nums, i + 1, right, k - i + left - 1)
