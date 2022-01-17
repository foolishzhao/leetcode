from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # 为什么不用 nums[low] 去比较 因为 mid有可能等于low, 但是不可能等于high
            # 这种情况下 nums[low] 一定等于nums[mid] ，但是这时 给high -1或者low +1 dous
            # 不合适的
            if nums[high] == nums[mid]:  # tricky part
                high -= 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]