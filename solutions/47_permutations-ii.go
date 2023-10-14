package solutions

import (
	"sort"
	"strconv"
)

func PermuteUnique(nums []int) [][]int {
	sort.Ints(nums)

	var r [][]int
	m := make(map[string]bool)
	var s string

	negMap := make(map[int]string, 10)

	for i := -1; i >= -10; i-- {
		c := string(97 - i)
		negMap[i] = c
	}

	for _, v := range nums {
		if v < 0 {
			s += negMap[v]
		} else {
			s += strconv.Itoa(v)
		}
	}

	var recur func([]int, string, int)

	recur = func(n []int, s string, i int) {
		if i == len(n) {
			if _, ok := m[s]; !ok {
				m[s] = true
				cpy := make([]int, len(n))
				copy(cpy, n)
				r = append(r, cpy)
			}
			return
		}

		for ii := i; ii < len(n); ii++ {
			if ii == i {
				recur(n, s, i+1)
			} else {
				tmp := []rune(s)
				tmp[i], tmp[ii] = tmp[ii], tmp[i]
				n[i], n[ii] = n[ii], n[i]
				recur(n, string(tmp), i+1)
				n[i], n[ii] = n[ii], n[i]
			}
		}
	}

	recur(nums, s, 0)

	return r
}
