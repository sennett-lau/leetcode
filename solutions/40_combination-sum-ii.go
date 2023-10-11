package solutions

import (
	"fmt"
	"sort"
)

func CombinationSum2(candidates []int, target int) [][]int {
	var result [][]int

	if len(candidates) == 0 {
		return result
	}

	sort.Ints(candidates)

	backtracking2(candidates, target, &result, make([]int, 0))

	return result
}

func backtracking2(c []int, t int, result *[][]int, tmp []int) {
	if t < 0 {
		return
	}

	if t == 0 {
		cpy := make([]int, len(tmp))
		copy(cpy, tmp)
		*result = append(*result, cpy)
	}

	for i := 0; i < len(c); i++ {
		if i > 0 && c[i] == c[i-1] {
			continue
		}
		tmp = append(tmp, c[i])
		fmt.Println(tmp)
		backtracking2(c[i+1:], t-c[i], result, tmp)
		tmp = tmp[:len(tmp)-1]
	}
}
