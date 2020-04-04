from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)
        median = self.findKthElement(nums, 0, n - 1, (n + 1) // 2)

        def vIdx(i, n):
            return (2 * i + 1) % (n | 1)

        i, j, k = 0, n - 1, 0
        while k <= j:
            if nums[vIdx(k, n)] > median:
                nums[vIdx(k, n)], nums[vIdx(i, n)] = nums[vIdx(i, n)], nums[vIdx(k, n)]
                i += 1
                k += 1
            elif nums[vIdx(k, n)] < median:
                nums[vIdx(k, n)], nums[vIdx(j, n)] = nums[vIdx(j, n)], nums[vIdx(k, n)]
                j -= 1
            else:
                k += 1

    def findKthElement(self, nums, left, right, k) -> int:
        if left == right:
            return nums[left]

        pivot = nums[left]
        i, j = left + 1, right
        while i <= j:
            if nums[i] <= pivot:
                nums[i - 1] = nums[i]
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        nums[j] = pivot

        if j - left + 1 == k:
            return pivot
        elif j - left + 1 > k:
            return self.findKthElement(nums, left, j - 1, k)
        else:
            return self.findKthElement(nums, j + 1, right, k - j + left - 1)
