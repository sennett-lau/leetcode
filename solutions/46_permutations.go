package solutions

func Permute(nums []int) [][]int {
	var r [][]int

	recur(nums, &r, 0)

	return r
}

func recur(n []int, r *[][]int, i int) {
	if i == len(n) {
		cpy := make([]int, len(n))
		copy(cpy, n)
		*r = append(*r, cpy)
		return
	}

	for ii := i; ii < len(n); ii++ {
		if ii == i {
			recur(n, r, i+1)
		} else {
			n[i], n[ii] = n[ii], n[i]
			recur(n, r, i+1)
			n[i], n[ii] = n[ii], n[i]
		}
	}
}
