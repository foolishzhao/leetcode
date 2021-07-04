from typing import List
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyPQ, sellPQ = list(), list()
        for p, m, t in orders:
            if t == 0:  # buy
                while sellPQ and sellPQ[0][0] <= p and m:
                    sellP, sellM = heapq.heappop(sellPQ)
                    if m < sellM:
                        heapq.heappush(sellPQ, (sellP, sellM - m))
                        m = 0
                    else:
                        m -= sellM

                if m:
                    heapq.heappush(buyPQ, (-p, m))
            else:  # sell
                while buyPQ and -buyPQ[0][0] >= p and m:
                    buyP, buyM = heapq.heappop(buyPQ)
                    if m < buyM:
                        heapq.heappush(buyPQ, (buyP, buyM - m))
                        m = 0
                    else:
                        m -= buyM

                if m:
                    heapq.heappush(sellPQ, (p, m))

        return (sum([m for _, m in buyPQ]) + sum([m for _, m in sellPQ])) % (10 ** 9 + 7)
