package solutions

func SingleNumber(nums []int) int {
	m := make(map[int]bool)
	d := make(map[int]bool)

	for i := 0; i < len(nums); i++ {
		_, ok1 := m[nums[i]]
		_, ok2 := d[nums[i]]

		if ok2 {
			continue
		} else if ok1 {
			delete(m, nums[i])
			d[nums[i]] = true
		} else {
			m[nums[i]] = true
		}
	}

	for k := range m {
		return k
	}

	return -1
}
