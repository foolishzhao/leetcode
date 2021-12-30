import heapq

class MedianFinder:
    def __init__(self):
        self.small = list()
        self.large = list()

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small)+1 < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        return (self.large[0]- self.large[0])/2



