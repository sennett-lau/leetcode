package solutions

func Intersection(nums1 []int, nums2 []int) []int {
	m := make(map[int]bool, len(nums1))
	saved := make(map[int]bool, len(nums1))
	var result []int

	for _, v := range nums1 {
		m[v] = true
	}

	for _, v := range nums2 {
		_, duplicate := m[v]
		_, counted := saved[v]

		if duplicate && !counted {
			result = append(result, v)
			saved[v] = true
		}
	}

	return result
}
