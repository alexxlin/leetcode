func insert(intervals [][]int, newInterval []int) [][]int {
    ledge, redge := newInterval[0], newInterval[1]
    l := len(intervals)
    if l == 0 {
        return [][]int{[]int{ledge, redge}}
    }
    ret := [][]int{}
    i := 0
    for i < l && intervals[i][1] < newInterval[0] {
        ret = append(ret, intervals[i])
        i++
    }

    for i < l && intervals[i][0] <= newInterval[1] {
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i++
    }
    ret = append(ret, newInterval)

    for i < l {
        ret = append(ret, intervals[i])
        i++
    }
    return ret
}
