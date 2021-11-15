class Solution:
    def isThree(self, n: int) -> bool:
        div = 0
        for i in range(2, n):
            div += n % i == 0
            if div > 1:
                return False
        return div == 1
