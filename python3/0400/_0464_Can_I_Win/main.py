class Solution:
    def __init__(self):
        self.memo = dict()

    def canIWin(self, n: int, d: int) -> bool:
        if n * (n + 1) // 2 < d:
            return False

        return self.helper(list(range(1, n + 1)), d)

    def helper(self, nums, d):
        key = str(nums)
        if key in self.memo:
            return self.memo[key]

        if nums[-1] >= d:
            self.memo[key] = True
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i + 1:], d - nums[i]):
                self.memo[key] = True
                return True

        self.memo[key] = False
        return False
