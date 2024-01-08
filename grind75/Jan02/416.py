class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # knapsack
        # check if we can reach sum(nums) / 2
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                if dp[j-num]:
                    dp[j] = True

        return dp[-1]
