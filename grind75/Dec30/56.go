func merge(intervals [][]int) [][]int {
    l := len(intervals)
    if l == 1 {
        return intervals
    }
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][0] == intervals[j][0] {
            return intervals[i][1] > intervals[j][1]
        } else {
            return intervals[i][0] < intervals[j][0]
        }
    })
    ret := make([][]int, 0, l)
    ret = append(ret, intervals[0])
    t := intervals[0][1]
    for i := 1; i < len(intervals); i++ {
        ch, ct := intervals[i][0], intervals[i][1]
        // fmt.Printf("h=%d t=%d ch=%d ct=%d\n", h,t,ch, ct)
        // case1
        if ch > t {
            ret = append(ret, intervals[i])
            t = ct
        }
        // case2
        if ch <= t && ct > t {
            ret[len(ret)-1][1] = ct
            t = ct
        }
    }
    return ret
}
