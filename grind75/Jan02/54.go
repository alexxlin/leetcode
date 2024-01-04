func spiralOrder(matrix [][]int) []int {
    ret := []int{}
    imin, jmin, imax, jmax := 0,0,len(matrix)-1, len(matrix[0])-1

    for imin <= imax && jmin <= jmax {
        for j := jmin; j <= jmax; j++ {
            ret = append(ret, matrix[imin][j])
        }
        for i := imin+1; i <= imax; i++ {
            ret = append(ret, matrix[i][jmax])
        }
        if imin < imax && jmin < jmax {
            for j := jmax-1; j >= jmin; j-- {
            ret = append(ret, matrix[imax][j])
        }
            for i := imax-1; i > imin; i-- {
                ret = append(ret, matrix[i][jmin])
            }
        }
    imin += 1
    jmin += 1
    imax -= 1
    jmax -= 1
    }

    return ret
}
