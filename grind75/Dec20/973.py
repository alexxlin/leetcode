from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> 
List[List[int]]:
        heap = []
        for point in points:
            heappush(heap, [-sqrt(abs(point[0]) ** 2 + abs(point[1] ** 
2)), point[0], point[1]])
            if len(heap) > k:
                heappop(heap)
        return [[p[1], p[2]] for p in heap]
