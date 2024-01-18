func nextPermutation(nums []int)  {
    n := len(nums)
    for i := n-1; i > 0; i-- {
        if nums[i-1] > nums[i] {
            continue
        }
        for j := n-1; j > i-1; j-- {
            if nums[j] <= nums[i-1] {
                continue
            }
            nums[i-1], nums[j] = nums[j], nums[i-1]
            t := nums[i:]
            sort.Ints(t)
            return
        }
    }
    sort.Slice(nums, func(i,j int) bool {
        return nums[i]<nums[j]
    })
    return
}
