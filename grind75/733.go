func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    dirs := [][]int{[]int{1,0}, []int{-1,0}, []int{0,1}, []int{0,-1},}
    m,n := len(image), len(image[0])
    visited := make([]int, m*n)
    old := image[sr][sc]
    var dfs func(int, int)
    dfs = func(i, j int) {
        for _, dir := range dirs {
            ni, nj := i+dir[0], j+dir[1]
            if ni < 0 || ni >= m || nj < 0 || nj >= n || visited[ni*n+nj] == 1 {
                continue
            }
            if image[ni][nj] != old {
                continue
            }
            image[ni][nj] = color
            visited[ni*n+nj] = 1
            dfs(ni,nj)
        }
    }
    visited[sr*n+sc] = 1
    image[sr][sc] = color
    dfs(sr, sc)
    return image
}
