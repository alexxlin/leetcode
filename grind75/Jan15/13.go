func romanToInt(s string) int {
    m := map[byte]int{
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000,
    }
    fmt.Println(m)
    prev := 0
    i := len(s)-1
    ret := 0
    for i >= 0 {
        val := m[s[i]]
        if val >= prev {
            ret += val
        } else {
            ret -= val
        }
        prev = val
        i--
    }
    return ret
}
