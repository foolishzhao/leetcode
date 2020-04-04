class Solution:
    def magicalString(self, n: int) -> int:
        if not n:
            return 0

        nums = [1, 2, 2]
        i, num = 2, 1
        while len(nums) < n:
            for _ in range(nums[i]):
                nums.append(num)

            i += 1
            # flip num between 1 and 2
            num ^= 3

        return nums[:n].count(1)
