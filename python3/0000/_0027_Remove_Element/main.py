


class Solution:
    def removeElement(self, nums, val) :
        if not nums:
            return 0
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1

        return i
if __name__ == '__main__':
    nums = [3,2,2,3]
    Solution().removeElement(nums,3)
    print(nums)