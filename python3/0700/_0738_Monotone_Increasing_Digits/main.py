class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums = [int(x) for x in list(str(N))]
        n, i = len(nums), 0
        while i < n - 1 and nums[i] <= nums[i + 1]:
            i += 1

        if i == n - 1:
            return N

        while i > 0 and nums[i] == nums[i - 1]:
            i -= 1

        nums[i] -= 1
        while i + 1 < n:
            nums[i + 1] = 9
            i += 1

        return int(''.join([str(x) for x in nums]))

    def monotoneIncreasingDigits2(self, N: int) -> int:
        nums = [int(x) for x in list(str(N))]
        n, end = len(nums), len(nums) - 1
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                end = i - 1
                nums[end] -= 1

        for i in range(end + 1, n):
            nums[i] = 9

        return int(''.join([str(x) for x in nums]))


if __name__ == '__main__':
    Solution().monotoneIncreasingDigits(10)
