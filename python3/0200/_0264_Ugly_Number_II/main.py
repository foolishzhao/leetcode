class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]

        p1, p2, p3 = 0, 0, 0
        while n > 1:
            t = min(nums[p1] * 2, nums[p2] * 3, nums[p3] * 5)
            nums.append(t)

            if nums[p1] * 2 == t:
                p1 += 1
            if nums[p2] * 3 == t:
                p2 += 1
            if nums[p3] * 5 == t:
                p3 += 1

            n -= 1

        return nums[-1]
