class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # merging, sort by begin time
        result = []
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            # has overlap
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            # no overlap
            else:
                result.append(interval)
        
        return result
