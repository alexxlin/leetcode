func twoSum(nums []int, target int) []int {
    m := map[int]int{}
    for k, v := range nums {
        if _, ok := m[target-v]; ok {
            return []int{k, m[target-v]}
        }
        m[v] = k
    }
    return []int{-1,-1}
}
