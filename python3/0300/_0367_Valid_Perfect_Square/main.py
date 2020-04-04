class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (right - left) // 2 + left
            t = mid * mid
            if t == num:
                return True
            elif t < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
