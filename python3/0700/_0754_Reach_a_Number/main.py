class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        step, cur = 0, 0
        while cur < target:
            step += 1
            cur += step

        while (cur - target) % 2:
            step += 1
            cur += step

        return step
