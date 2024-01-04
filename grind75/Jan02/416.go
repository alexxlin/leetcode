func canPartition(nums []int) bool {
    m := map[string]bool{}
    target := 0
    for i := 0; i < len(nums); i++ {
        target += nums[i]
    }
    if target % 2 != 0 {
        return false
    }
    
    var dfs func(int, int) bool
    dfs = func(idx, cur int) bool {
        k := fmt.Sprintf("%d-%d", cur, idx)
        if cur == 0 {
            return true
        }
        if cur < 0 || idx >= len(nums) {
            return false
        }
        if r, ok := m[k]; ok {
            return r
        }
        ret := dfs(idx+1, cur-nums[idx]) || dfs(idx+1, cur)
        m[k] = ret
        return ret
    }
    return dfs(0, target/2)
}
