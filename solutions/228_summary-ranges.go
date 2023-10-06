package solutions

import (
	"strconv"
)

func SummaryRanges(nums []int) []string {
	result := []string{}

	str := ""

	for i := 0; i < len(nums); {
		str = str + strconv.Itoa(nums[i])

		j := i + 1

		for ; j < len(nums) && nums[j]-nums[j-1] == 1; j++ {
		}

		if i != j-1 {
			str = str + "->" + strconv.Itoa(nums[j-1])
		}

		result = append(result, str)

		str = ""
		i = j
	}

	return result
}
