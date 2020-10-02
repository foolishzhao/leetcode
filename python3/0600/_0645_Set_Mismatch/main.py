from typing import List


class Solution:
    # O(n) time complexity, O(n) space complexity
    def findErrorNums(self, nums: List[int]) -> List[int]:
        st, res = set(), list()
        for num in nums:
            if num in st:
                res.append(num)
            st.add(num)

        for i in range(len(nums)):
            if i + 1 not in st:
                res.append(i + 1)
                break
        return res

    # O(n) time complexity, O(n) space complexity
    def findErrorNums2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [sum(nums) - sum(set(nums)), n * (n + 1) // 2 - sum(set(nums))]

    # O(n) time complexity, O(1) space complexity
    def findErrorNums3(self, nums: List[int]) -> List[int]:
        res = list()
        for num in nums:
            j = abs(num) - 1
            if nums[j] > 0:
                nums[j] = -nums[j]
            else:
                res.append(j + 1)

        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = -nums[i]
            else:
                res.append(i + 1)

        return res
