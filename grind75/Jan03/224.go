func calculate(s string) int {
    ops := []int{1}
    sign := 1
    ret := 0
    for i := 0; i < len(s); {
        switch s[i] {
        case ' ':
            i++
        case '+':
            sign = ops[len(ops)-1]
            i++
        case '-':
            sign = -1*ops[len(ops)-1]
            i++
        case '(':
            ops = append(ops, sign)
            i++
        case ')':
            ops = ops[:len(ops)-1]
            i++
        default:
            num := 0
            for ; i < len(s) && '0' <= s[i] && s[i] <= '9'; i++ {
                num = num*10+int(s[i]-'0')
            }
            ret += sign*num
        }
    }
    return ret
}
