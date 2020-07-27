class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for i in range(0, len(nums), 2):
            
            freq = nums[i]
            val = nums[i+1]
            
            #method one for appending list
            # for j in range(freq):
            #     result.append(val)

            #method two for appending list
            result.extend([val] * freq)
                
        return result
