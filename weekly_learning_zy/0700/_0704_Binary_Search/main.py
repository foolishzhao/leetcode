from typing import List


class Solution:
    def binarySearch(self,nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
        return self.binarySearch(nums, left, right, target)

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
        return -1


        # return self.binarySearch(nums, 0, len(nums) - 1, target)
if __name__ == '__main__':
    nums = [3,2,5,8,6,9]
    print(Solution().search(nums,5))
