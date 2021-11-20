class Solution:
    def removeElement(self,nums,val):
        while val in nums: nums.remove(val)

    def removeElement2(self,nums,val) :
        if not nums:
            return 0
        i = 0
        for num in nums:
            if num != val:
                nums[i]=num
                i += 1
        return i



if __name__ == '__main__':
    nums = [-1, 0, 1, 2,-1,-1, -4]
    p = Solution().removeElement2(nums,-1)
    print p
    print(nums[0:p])