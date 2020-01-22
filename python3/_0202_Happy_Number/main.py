class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while slow != 1 and fast != 1:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
            if slow == fast:
                break

        return slow == 1 or fast == 1

    def getNext(self, n: int) -> int:
        res = 0
        while n:
            t = n % 10
            res += t * t
            n //= 10

        return res


if __name__ == '__main__':
    Solution().isHappy(19)
