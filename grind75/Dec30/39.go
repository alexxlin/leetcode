func combinationSum(candidates []int, target int) [][]int {
    ret := [][]int{}
    sort.Ints(candidates)
    n := len(candidates)
    var dfs func([]int, int, int)
    dfs = func(cur []int, idx int, sum int) {
        if sum == target {
            ret = append(ret, cur)
            return
        }
        for i := idx; i < n; i++ {
            if sum+candidates[i] > target {
                break
            }
            tmp := append([]int{}, cur...)
            tmp = append(tmp, candidates[i])
            dfs(tmp, i, sum+candidates[i])
        }
    }
    dfs([]int{}, 0, 0)
    return ret
}
