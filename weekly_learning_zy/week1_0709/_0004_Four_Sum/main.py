class Solution:

    def fourSum(self,nums,target):
        res =[]
        lent = len(nums)
        nums.sort()
        for j in range(0,lent-3):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            target_tmp = target-nums[j]
            for i in range(j+1,lent-2):
                newtarget = target_tmp-nums[i]
                left=i+1
                right=lent-1
                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue
                while(left < right):
                    if nums[left]+nums[right]==newtarget:
                        res.append([nums[j], nums[i],nums[left], nums[right]])
                        while left < lent - 1 and nums[left] == nums[left + 1]:
                            left = left + 1
                        while right > 0 and nums[right] == nums[right - 1]:
                            right = right - 1
                        right = right - 1
                        left = left + 1
                    elif nums[left]+nums[right] > newtarget:
                        right=right-1
                    else:
                        left=left+1

        return res



if __name__ == '__main__':
    ress = Solution().fourSum([2,2,2,2,2],8)
    print(ress)



