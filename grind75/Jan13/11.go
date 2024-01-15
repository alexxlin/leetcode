func maxArea(height []int) int {
    i,j := 0, len(height)-1
    ret := 0
    for i < j {
        ret = max(ret, (j-i)*min(height[i], height[j]))
        if height[i] < height[j] {
            i++
        } else {
            j--
        }
    }
    return ret
}
