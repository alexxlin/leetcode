class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = -math.inf
        cumulative_sum = 0

        for num in nums:
            if cumulative_sum <= 0:
                cumulative_sum = num
            else:
                cumulative_sum += num
            
            largest = max(largest, cumulative_sum)
        
        return largest
