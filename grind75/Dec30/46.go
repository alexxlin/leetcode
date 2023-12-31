func permute(nums []int) [][]int {
    ret := [][]int{}
    n := len(nums)
    visited := make([]int, n)
    var dfs func([]int)
    dfs = func(cur []int) {
        if len(cur) == n {
            ret = append(ret, cur)
            return
        }
        for i := 0; i < n; i++ {
            if visited[i] == 1 {
                continue
            }
            tmp := append([]int{}, cur...)
            tmp = append(tmp, nums[i])
            visited[i] = 1
            dfs(tmp)
            visited[i] = 0
        }
    }
    dfs([]int{})
    return ret
}
