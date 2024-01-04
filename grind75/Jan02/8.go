func myAtoi(s string) int {
    i := 0
    n := len(s)
    pos := true
    ret := 0
    for i < n && s[i] == ' ' {
        i++
    }
    if i >= n {
        return ret
    }
    if s[i] < '0' || s[i] > '9' {
        if s[i] == '-' || s[i] == '+' {
            pos = (s[i] == '+')
            i++
        } else {
            return ret
        }
    }
    
    intmin, intmax := -1<<31, 1<<31 - 1 
    for i < n && s[i] >= '0' && s[i] <= '9' {
        ret = ret * 10 + int(s[i]- '0')
        i++
        if !pos && -1*ret < intmin {
            return intmin
        }
        if pos && ret > intmax {
            return intmax
        }
    }
    
    if !pos {
        return -1*ret
    }
    return ret
}
