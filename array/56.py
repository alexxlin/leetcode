class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #time: O(nlogn) for sorting
        #space: O(n)
        
        #basecase
        if intervals == []:
            return []
        
        #sort the intervals based on left endpoints
        intervals.sort(key = lambda x: x[0])
        
        
        result = []
        
        for i in range(len(intervals)):
                        
                
            #check if the left endpoint is less than the right endpoint
            #of previous interval, if so, overlapping
            if len(result) != 0 and intervals[i][0] <= result[-1][1]:
                
                #change the right endpoint of the merged
                #interval to max of the two overlapping intervals
                result[-1][1] = max(result[-1][1], intervals[i][1])
                                
                    
            #current element not overlapping with next element, just append it
            else:
                result.append(intervals[i])
            
        
        return result
        