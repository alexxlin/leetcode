func search(nums []int, target int) int {
    l, r := 0, len(nums)-1

    for l <= r {
        m := l+(r-l)>>1
        if nums[m] == target {
            return m
        }
        if nums[m] < nums[r] {
            if target <= nums[r] && target > nums[m] {
                l = m+1
            } else {
                r = m-1
            }
        } else { // nums[m] > nums[r]
            if target >= nums[l] && target < nums[m] {
                r = m-1
            } else {
                l = m+1
            }
        }
    }
    return -1
}
