class Solution:
    def threeSumClosest(self,nums,target):
        lent = len(nums)
        nums.sort()
        ans = float('inf')
        res = 0
        for k in range(0 ,lent-3):
            newtarget = target-nums[k]
            left = k+1
            right = lent-1
            while left < right:
                sums = nums[right]+nums[left]
                check = sums + nums[k]
                if (abs(check-target)<ans):
                    ans = abs(check-target)
                    if(ans == 0):
                        return check
                    res = check
                if(sums > newtarget):
                    right=right-1
                else:
                    left=left+1
        return res
if __name__ == '__main__':
    ress = Solution().threeSumClosest([-1, 2, 1, -4,1],1)
    print(ress)



