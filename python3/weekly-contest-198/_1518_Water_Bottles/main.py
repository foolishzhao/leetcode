class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res, empty = numBottles, numBottles
        while empty >= numExchange:
            add = empty // numExchange
            empty %= numExchange
            res += add
            empty += add
        return res
