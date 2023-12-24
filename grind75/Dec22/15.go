func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    size := len(nums)
    ret := [][]int{}
    if len(nums) < 3 { return ret }
    for i := 0; i < size-2; i++ {
        if i > 0 && nums[i] == nums[i-1] { 
            continue
        }

        j,k := i+1,size-1

        for j < k {
            sum := nums[i]+nums[j]+nums[k]

            if sum < 0 {
                j++
                for j < k && nums[j] == nums[j-1] {
                    j++
                }
            } else { // sum >= 0
                if sum == 0 {
                    ret = append(ret, []int{nums[i], nums[j], nums[k]})
                    j++
                    for j < k && nums[j] == nums[j-1] {
                        j++
                    }
                } else { // sum > 0
                    k--
                    for j < k && nums[k] == nums[k+1] {
                        k--
                    }
                }   
            }
        }
    }
    return ret
}
