from typing import List


class Solution:
    def firstMissingPositive1(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res

    def firstMissingPositive2(self, nums: List[int]) -> int:
        nums.sort()
        ans = float("-inf")
        for i in range(0, max(max(nums) + 1, 2)):
            if i == max(nums):
                ans = max(nums) + 1
            if i not in nums:
                ans = i
                if ans <= 0:
                    continue
                else:
                    break
        return ans

    # O(n)
    def firstMissingPositive(self, nums):

        for i in range(len(nums)):
            # 我们期待nums[nums[i]-1] = nums[i]
            # 如果 nums[nums[i] - 1] != nums[i]:
            # 说明当前位置i 的 nums[i】是个错的值， 需要把这个值换到下标为nums[i] - 1 的位置上去
            # 如果是正确的就不需要做什么
            # 然后要考虑缓过来的这个数现在是否在正确的位置 所以使用while循环
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    arr = [3, 4, -1, 1]
    ans = Solution().firstMissingPositive(arr)
    print("----answser-----")
    print(ans)
