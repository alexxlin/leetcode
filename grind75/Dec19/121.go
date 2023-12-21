func maxProfit(prices []int) int {
    buy, sell := math.MinInt, 0
    for _, v := range prices {
        buy = max(buy, -1*v)
        sell = max(sell, buy+v)
    }
    return sell
}
