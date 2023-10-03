package solutions

func MaxProfit(prices []int) int {
	l := len(prices)

	if l == 1 {
		return 0
	}

	s := prices[0]
	p := 0

	for i := 1; i < l; i++ {
		if prices[i] < s {
			s = prices[i]
		} else if prices[i]-s > p {
			p = prices[i] - s
		}
	}

	return p
}
