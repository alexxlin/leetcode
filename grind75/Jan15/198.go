func rob(nums []int) int {
    n := len(nums)
    if n == 1 { return nums[0] }
    if n == 2 { return max(nums[0], nums[1]) }
    dp := make([]int, n)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    ret := 0
    for i := 2; i < n; i++ {
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        ret = max(ret, dp[i])
    }
    return ret
}   

