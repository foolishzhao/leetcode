class Solution:
    def twosum(self, nums, target):
        for i in range(len(nums)):
            num = target-nums[i]
            if num in nums[i+1:]:
                print i, nums.index(num, i+1)
                return [i, nums.index(num, i+1)]
    def twosum2(self,nums,target):
        nums_dict = {}
        for i,num in enumerate(nums):
            if num in nums_dict:
                print nums_dict[num], i
                return [nums_dict[num], i]
            else:
                nums_dict[target - num] = i
if __name__ == '__main__':
    Solution().twosum2([3,7,9,8], 17)