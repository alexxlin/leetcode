func isValidSudoku(board [][]byte) bool {
    col, row, box := [9][9]int{}, [9][9]int{}, [9][9]int{}
    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            if board[i][j] == '.' { continue }
            num := int(board[i][j]-'0')
            bidx := (i/3)*3+(j/3)
            if col[i][num-1] == 1 || row[j][num-1] == 1 || box[bidx][num-1] == 1 {
                return false
            }
            col[i][num-1] = 1
            row[j][num-1] = 1
            box[bidx][num-1] = 1
        }
    }
    return true
}
