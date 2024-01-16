func canAttendMeetings(intervals [][]int) bool {
    if len(intervals) <= 1 { return true }
    sort.Slice(intervals, func(i,j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    i, j := 0, 1
    for j < len(intervals) {
        if intervals[i][1] > intervals[j][0] {
            return false
        }
        i++
        j++
    }
    return true
}
