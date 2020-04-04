class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False

        rx = 0
        while x > rx:
            if rx == x // 10:
                break

            rx = rx * 10 + x % 10
            x //= 10

        return x == rx or rx == (x // 10)
