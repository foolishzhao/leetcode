from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def getNext(i):
            return (i + nums[i]) % len(nums)

        for i, num in enumerate(nums):
            if num:
                slow, fast = i, getNext(i)
                while nums[fast] * nums[i] > 0 and nums[getNext(fast)] * nums[i] > 0:
                    if slow == fast:
                        if slow == getNext(slow):
                            break
                        return True
                    slow = getNext(slow)
                    fast = getNext(getNext(fast))

                slow, v = i, nums[i]
                while nums[slow] * v > 0:
                    ns = getNext(slow)
                    nums[slow] = 0
                    slow = ns

        return False
