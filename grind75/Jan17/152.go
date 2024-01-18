func maxProduct(nums []int) int {
    neg, pos, ret := nums[0], nums[0], nums[0]
    for i := 1; i < len(nums); i++ {
        negp, posp := neg, pos
        pos = max(nums[i], max(nums[i]*posp, nums[i]*negp))
        neg = min(nums[i], min(nums[i]*posp, nums[i]*negp))
        ret = max(ret, pos)
    }
    return ret
}

