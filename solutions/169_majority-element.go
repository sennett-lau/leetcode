package solutions

func MajorityElement(nums []int) int {
	m := make(map[int]int)

	for _, v := range nums {
		m[v]++
	}

	max := 0
	result := 0

	for k, v := range m {
		if v > max {
			result = k
			max = v
		}
	}

	return result
}
