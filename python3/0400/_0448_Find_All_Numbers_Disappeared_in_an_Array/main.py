from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n, i = len(nums), 0
        while i < n:
            if nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                t = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = t
            else:
                i += 1

        return [i + 1 for i, x in enumerate(nums) if x != i + 1]


if __name__ == '__main__':
    nums = [3, 4, 1, 2, 5]
    i = 0
    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    print(nums)

    i = 1
    nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
    print(nums)
