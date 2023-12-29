func strStr(haystack string, needle string) int {
    i, j := 0, 0
    for i < len(haystack) && j < len(needle) {
        if haystack[i] == needle[j] {
            i++
            j++
        } else {
            i = i-j+1
            j = 0
        }
    }
    if j == len(needle) {
        return i-len(needle)
    }
    return -1
}
