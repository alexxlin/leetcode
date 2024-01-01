func majorityElement(nums []int) int {
    ret := -1
    cnt := 0
    for _, val := range nums {
        if cnt == 0 {
            ret = val
            cnt++
        } else {
            if val == ret {
                cnt++
            } else {
                cnt--
            }
        }
    }
    return ret
}
