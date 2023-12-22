func kClosest(points [][]int, k int) [][]int {
    sort.Slice(points, func(i, j int) bool {
        a := points[i][0]*points[i][0]+ points[i][1]*points[i][1]
        b := points[j][0]*points[j][0]+ points[j][1]*points[j][1]
        return a < b
    })
    return points[:k]
}
