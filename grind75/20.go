func isValid(s string) bool {
    stack := []string{}
    ss := strings.Split(s, "")

    for _, val := range ss {
        if val == "(" || val == "[" || val == "{" {
            stack = append(stack, val)
            continue
        }
        if val == ")" && (len(stack) == 0 || stack[len(stack)-1] != "(") {
            return false
        }
        if val == "]" && (len(stack) == 0 || stack[len(stack)-1] != "[") {
            return false
        }
        if val == "}" && (len(stack) == 0 || stack[len(stack)-1] != "{") {
            return false
        }
        stack = stack[:len(stack)-1]
    }

    return len(stack) == 0
}
