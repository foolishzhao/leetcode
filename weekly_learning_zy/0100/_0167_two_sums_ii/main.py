from _ast import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(numbers):
            if num in nums_dict:
                return [nums_dict[num] + 1, i + 1]
            else:
                nums_dict[target - num] = i
