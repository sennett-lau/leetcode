package solutions

func PlusOne(digits []int) []int {
	var result []int

	i := len(digits) - 1
	incr := 0
	isPlusOne := true

	for i >= 0 {
		num := digits[i] + incr

		if isPlusOne {
			num++
			isPlusOne = false
		}

		if num >= 10 {
			incr = 1
			num = num % 10
		} else {
			incr = 0
		}

		result = append([]int{num}, result...)

		i--
	}

	if incr > 0 {
		result = append([]int{incr}, result...)
	}

	return result
}
