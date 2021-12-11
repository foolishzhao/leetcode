from typing import List


class Solution:
    def twosum(self, nums, target):
        for i in range(len(nums)):
            num = target-nums[i]
            if num in nums[i+1:]:
                print(i, nums.index(num))
                return [i, nums.index(num, i+1)]
    def twosum2(self,nums,target):
        nums_dict = {}
        for i,num in enumerate(nums):
            if num in nums_dict:
                print (nums_dict[num], i)
                return [nums_dict[num], i]
            else:
                nums_dict[target - num] = i

    def twosum3(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                res.append(i)
                res.append(nums.index(target - nums[i], i+1))
        return res


if __name__ == '__main__':
    ans = Solution().twosum3([3,3], 6)
    print(ans)