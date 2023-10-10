package solutions

func CombinationSum(candidates []int, target int) [][]int {
	var result [][]int

	if len(candidates) == 0 {
		return result
	}

	backtracking(candidates, target, 0, &result, make([]int, 0))

	return result
}

func backtracking(c []int, t int, i int, result *[][]int, tmp []int) {
	if t < 0 || i > len(c) {
		return
	}

	if t == 0 {
		cpy := make([]int, len(tmp))
		copy(cpy, tmp)
		*result = append(*result, cpy)
	}

	for j := i; j < len(c); j++ {
		tmp = append(tmp, c[j])
		backtracking(c, t-c[j], j, result, tmp)
		tmp = tmp[:len(tmp)-1]
	}
}
