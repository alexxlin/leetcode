class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        # if num is candidate, +1, else -1
        # change candidate whenever it switches sign
        # for the majority, it will stay as candidate as the count will 
stay positive
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
