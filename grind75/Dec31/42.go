func trap(height []int) int {
    pivot := - 1
    curmax := math.MinInt
    for i := 0; i < len(height); i++ {
        if height[i] > curmax {
            curmax = height[i]
            pivot = i
        }
    }
    ret := 0
    curmax = -1
    for i := 0; i < pivot; i++ {
        if height[i] >= curmax {
            curmax = height[i]
        } else {
            ret += curmax-height[i]
        }
    }

    curmax = -1
    for i := len(height)-1; i > pivot; i-- {
        if height[i] >= curmax {
            curmax = height[i]
        } else {
            ret += curmax-height[i]
        }
    }
    return ret
}
