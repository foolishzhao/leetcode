class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n, i = len(nums), 0
        while i < n - 1 and nums[i] >= nums[i + 1]:
            i += 1

        if i == n - 1:
            return num

        j = i + 1
        for k in range(i + 2, n):
            if nums[k] >= nums[j]:
                j = k

        for k in range(i + 1):
            if nums[k] < nums[j]:
                nums[k], nums[j] = nums[j], nums[k]
                break

        return int("".join(nums))

    def maximumSwap2(self, num: int) -> int:
        nums = list(str(num))
        last = {x: i for i, x in enumerate(nums)}
        for i, x in enumerate(nums):
            for d in range(9, 0, -1):
                y = str(d)
                if y > x and y in last and last[y] > i:
                    j = last[y]
                    nums[i], nums[j] = nums[j], nums[i]
                    return int("".join(nums))
        return int("".join(nums))
