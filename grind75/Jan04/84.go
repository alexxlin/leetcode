func largestRectangleArea(heights []int) int {
    heights = append([]int{0}, heights...)
    heights = append(heights, 0)
    stack := []int{}
    ret := 0
    for i := 0; i < len(heights); i++ {
        if len(stack) == 0 || heights[i] >= heights[stack[len(stack)-1]] {
            stack = append(stack, i)
            continue
        }
        for heights[stack[len(stack)-1]] > heights[i] {
            idx := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            ret = max(ret, heights[idx]*(i-stack[len(stack)-1]-1))
        }
        stack = append(stack, i)
    }
    return ret
}   

