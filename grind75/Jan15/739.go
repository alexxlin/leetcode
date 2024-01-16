func dailyTemperatures(temperatures []int) []int {
    n := len(temperatures)
    ret := make([]int, n)
    if n == 1 { return ret }
    stack := []int{0}
    for i := 1; i < n; i++ {
        idx := stack[len(stack)-1]
        if temperatures[i] <= temperatures[idx] {
            stack = append(stack, i)
            continue
        }
        for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]]{
            pop := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            ret[pop] = i-pop
        }
        stack = append(stack, i)
    }
    return ret
}
