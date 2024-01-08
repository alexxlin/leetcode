from heapq import heappush, heappop
class MedianFinder:
    # use two heaps, max heap for the first half, min heap for the 
second half
    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        # inserting into min heap, need to insert into max heap first, 
then insert into min heap
        if len(self.max) == len(self.min):
            heappush(self.max, -num)
            heappush(self.min, -heappop(self.max))
        # inserting into max heap
        else:
            heappush(self.min, num)
            heappush(self.max, -heappop(self.min))

    def findMedian(self) -> float:
        if len(self.min) > len(self.max):
            return self.min[0]
        return (self.min[0] - self.max[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
