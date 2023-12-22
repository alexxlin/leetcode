func maxSubArray(nums []int) int {
    ret := math.MinInt
    cur := 0
    for _, val := range nums {
        if cur <= 0 { 
            cur = val 
        } else { 
            cur = val+cur 
        }
        ret = max(ret, cur)
    }
    return ret
}
