func subsets(nums []int) [][]int {
    ret := [][]int{}
    var dfs func(int, []int)
    dfs = func(idx int, cur []int) {
        ret = append(ret, cur)
        for i := idx; i < len(nums); i++ {
            tmp := append([]int{}, cur...)
            tmp = append(tmp, nums[i])
            dfs(i+1, tmp)
        }
    }
    dfs(0, []int{})
    return ret
}
