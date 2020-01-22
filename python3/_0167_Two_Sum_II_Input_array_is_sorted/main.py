from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        i, j = 0, len(numbers) - 1
        while i < j:
            t = numbers[i] + numbers[j]
            if t == target:
                return [i + 1, j + 1]
            elif t > target:
                j -= 1
            else:
                i += 1

        return []
