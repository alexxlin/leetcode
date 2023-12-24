func evalRPN(tokens []string) int {
    stack := []string{}

    for _, token := range tokens {
        if _, ok := strconv.Atoi(token); ok == nil {
            stack = append(stack, token)
            continue
        }
        if len(stack) < 2 { return -1 }
        l, _ := strconv.Atoi(stack[len(stack)-2])
        r, _ := strconv.Atoi(stack[len(stack)-1])
        stack = stack[:len(stack)-2]
        tmp := 0
        if token == "+" { tmp = l+r }
        if token == "-" { tmp = l-r }
        if token == "*" { tmp = l*r }
        if token == "/" { tmp = l/r }
        stack = append(stack, strconv.Itoa(tmp))
    }
    
    if len(stack) != 1 { return -1 }
    ret, _ := strconv.Atoi(stack[0])
    return ret
}
