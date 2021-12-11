class Solution:
    res = 0
    def totalNQueens(self, n):
        self.dfs([-1]*n, 0, self.res)
        return self.res


    def dfs(self, nums, index, res):
        if index == len(nums):
            self.res += 1
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index+1, self.res)


    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n -i or nums[i] == nums[n]:
                return False
        return True

        
