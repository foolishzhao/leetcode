class Solution:
    def threesum(self,nums):
        res = []
        lent = nums.__len__()
        nums.sort()
        i=0
        while i<lent-2:
            left = i+1
            right = lent-1
            while left<right:
                if nums[left]+nums[right] == -nums[i]:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<lent-1 and nums[left]==nums[left+1]:
                        left=left+1
                    while right>0 and nums[right]==nums[right-1]:
                        right=right-1
                    right=right-1
                    left=left+1
                elif nums[left]+nums[right]>-nums[i]:
                    right = right-1
                else:
                    left = left+1
            while i<lent-2 and nums[i]==nums[i+1]:
                i=i+1
            i=i+1
        print res
        return res
if __name__ == '__main__':
    Solution().threesum([-1, 0, 1, 2, -1, -4])

