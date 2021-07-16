class Solution:
    def removeElement(self,nums,val):
        while val in nums: nums.remove(val)

if __name__ == '__main__':
    nums = [-1, 0, 1, 2,-1,-1, -4]
    Solution().removeElement(nums,-1)
    print(nums)