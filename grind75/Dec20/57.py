class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) 
-> List[List[int]]:
        new_intervals = []
        inserted = False
        for i, interval in enumerate(intervals):
            # before the overlap
            if interval[1] < newInterval[0]:
                new_intervals.append(interval)
            elif interval[0] > newInterval[1]:
                    new_intervals.append(newInterval)
                    return new_intervals + intervals[i:]
            else:
                # in overlap
                newInterval = [min(interval[0], newInterval[0]), 
max(interval[1], newInterval[1])]
        
        new_intervals.append(newInterval)
        return new_intervals
