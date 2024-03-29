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

    def test(self,nums):
        print nums[1:5]
        print nums[:]
        print nums[1:3]
        print sum(nums[-2:-3])
        nums.append('ddd')
        print nums[:]
        del nums[len(nums)-1]
        print nums[:]
    def threeSumClo(self,nums,target):
        l = len(nums)
        nums.sort()

if __name__ == '__main__':
    ress = Solution().threeSumClosest([-1, 2, 1, -4,1],1)
    print(ress)
    ##Solution().test([1,2,3,4,5,6])



