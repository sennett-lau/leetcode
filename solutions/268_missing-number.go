package solutions

func MissingNumber(nums []int) int {
	m := make(map[int]bool, len(nums))

	for i := 0; i <= len(nums); i++ {
		m[i] = true
	}

	for _, v := range nums {
		delete(m, v)
	}

	for k := range m {
		return k
	}

	return -1
}
