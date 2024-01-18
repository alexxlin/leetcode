func solveSudoku(board [][]byte)  {
    col, row, box := [9][9]int{}, [9][9]int{}, [9][9]int{}
    m,n := len(board), len(board[0])
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if board[i][j] == '.' { continue }
            num := int(board[i][j]-'0')
            col[i][num-1] = 1
            row[j][num-1] = 1
            bidx := (i/3)*3+(j/3)
            box[bidx][num-1] = 1
        }
    }
    var dfs func(int, int) bool
    dfs = func(i, j int) bool {
        // base case
        if j == n {
            i++
            j = 0
        }
        if i == m {
            return true
        }
        if board[i][j] != '.' {
            return dfs(i, j+1)
        }
        for num := 1; num <= 9; num++ {
            boxidx := (i/3)*3+(j/3)
            if col[i][num-1] != 0 || row[j][num-1] != 0 || box[boxidx][num-1] != 0 {
                continue
            } 
            col[i][num-1] = 1
            row[j][num-1] = 1
            box[boxidx][num-1] = 1
            board[i][j] = byte(num)+'0'
            if dfs(i, j+1) {
                return true
            }
            col[i][num-1] = 0
            row[j][num-1] = 0
            box[boxidx][num-1] = 0
            board[i][j] = '.'
        }
        return false
    } 
    dfs(0,0)
}
