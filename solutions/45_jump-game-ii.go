package solutions

func Jump(nums []int) int {
	if len(nums) == 1 {
		return 0
	}

	curr := 0
	count := 0
	max := 0

	for i, v := range nums {
		if i + v > max {
			max = i + v
		}

		if i == curr {
			count++
			if max >= len(nums)-1 {
				return count
			}
			curr = max
		}
	}

	return -1
}
