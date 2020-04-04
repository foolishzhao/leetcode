class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        n = len(nums)
        i = n - 1
        while i and nums[i] <= nums[i - 1]:
            i -= 1

        if not i:
            return -1

        j = i
        while j < n and nums[j] > nums[i - 1]:
            j += 1
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]

        res = int("".join(nums[:i] + sorted(nums[i:])))
        return res if res < (1 << 31) else -1
