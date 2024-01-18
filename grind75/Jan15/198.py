class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                dp[i] = num
            elif i == 1:
                dp[i] = max(dp[i-1], num)
            else:
                dp[i] = max(dp[i-1], dp[i-2] + num)
        return dp[-1]
