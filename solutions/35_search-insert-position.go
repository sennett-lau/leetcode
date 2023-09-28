package solutions

func SearchInsert(nums []int, target int) int {
	s := 0
	e := len(nums) - 1

	if nums[0] >= target {
		return 0
	} else if nums[e] == target {
		return e
	} else if nums[e] < target {
		return e + 1
	}

	for s < e {
		if s == e-1 {
			return s + 1
		}

		m := (s + e) / 2
		if nums[m] == target {
			return m
		} else if nums[m] < target {
			s = m
		} else {
			e = m
		}
	}

	return s + 1
}
