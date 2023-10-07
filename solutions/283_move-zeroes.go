package solutions

func MoveZeroes(nums []int) {
	s := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[s] = nums[s], nums[i]
			s++
		}
	}
}
