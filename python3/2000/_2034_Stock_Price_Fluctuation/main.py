import heapq


class StockPrice:

    def __init__(self):
        self.current_ts = 0
        self.prices = dict()
        self.minHeap = list()
        self.maxHeap = list()

    def update(self, timestamp: int, price: int) -> None:
        self.current_ts = max(self.current_ts, timestamp)
        self.prices[timestamp] = price
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.current_ts]

    def maximum(self) -> int:
        while True:
            p, ts = heapq.heappop(self.maxHeap)
            if -p == self.prices[ts]:
                heapq.heappush(self.maxHeap, (p, ts))
                break
        return -p

    def minimum(self) -> int:
        while True:
            p, ts = heapq.heappop(self.minHeap)
            if p == self.prices[ts]:
                heapq.heappush(self.minHeap, (p, ts))
                break
        return p
