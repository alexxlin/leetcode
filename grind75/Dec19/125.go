

func isPalindrome(s string) bool {
    i, j := 0, len(s)-1
    s = strings.ToLower(s)
    for i < j {
        if (s[i] < 'A' || s[i] > 'Z') && (s[i] < 'a' || s[i] > 'z') && (s[i] < '0' || s[i] > '9') {
            i++
            continue
        }
        if (s[j] < 'A' || s[j] > 'Z') && (s[j] < 'a' || s[j] > 'z') && (s[j] < '0' || s[j] > '9') {
            j--
            continue
        }
        if s[i] != s[j] { return false }
        i++
        j--
    }
    return true
}
