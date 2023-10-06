package solutions

func ContainsDuplicate(nums []int) bool {
	m := make(map[uint64]bool)

	for _, v := range nums {
		if _, ok := m[uint64(v)]; ok {
			return true
		}
		m[uint64(v)] = true
	}

	return false
}
