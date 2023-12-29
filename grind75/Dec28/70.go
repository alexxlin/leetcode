func climbStairs(n int) int {
    one, two := 1, 2
    if n == 1 { return one }
    if n == 2 { return two }
    for i := 3; i <= n; i++ {
        tmp := one + two
        one = two
        two = tmp
    }
    return two
}
