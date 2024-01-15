func containsDuplicate(nums []int) bool {
    m := map[int]struct{}{}
    for _, v := range nums {
        if _, ok := m[v]; ok {
            return true
        }
        m[v] = struct{}{}
    }
    return false
}
