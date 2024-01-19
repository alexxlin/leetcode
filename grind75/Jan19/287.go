func findDuplicate(nums []int) int {
    for i := 0; i < len(nums); i++ {
        for nums[i] != nums[nums[i]-1] {
            tmp := nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
        }
    }
    for i := 0; i < len(nums); i++ {
        if nums[i]-1 != i {
            return nums[i]
        }
    }
    return -1
}
