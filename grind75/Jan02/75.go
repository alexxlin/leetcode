func sortColors(nums []int)  {
    n := len(nums)
    i,j := 0, n-1

    for cur := 0; cur < n; cur++ {
        for cur <= j && nums[cur] == 2 {
            nums[cur], nums[j] = nums[j], nums[cur]
            j--
        }
        if nums[cur] == 0 {
            nums[cur], nums[i] = nums[i], nums[cur]
            i++
        }
    }
    return
}
