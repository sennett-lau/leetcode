package solutions

func SearchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}

	return []int{searchLeft(nums, target), searchRight(nums, target)}
}

func searchLeft(nums []int, target int) int {
	l := 0
	r := len(nums) - 1

	for l < r {
		m := (l + r) / 2

		if nums[m] < target {
			l = m + 1
		} else {
			r = m
		}
	}

	if nums[l] == target {
		return l
	}

	return -1
}

func searchRight(nums []int, target int) int {
	l := 0
	r := len(nums) - 1

	for l < r {
		m := (l+r)/2 + 1

		if nums[m] > target {
			r = m - 1
		} else {
			l = m
		}
	}

	if nums[l] == target {
		return l
	}

	return -1

}
