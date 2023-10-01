package solutions

func Generate(numRows int) [][]int {
	var result [][]int

	result = append(result, []int{1})

	for i := 1; i < numRows; i++ {
		var row []int

		row = append(row, 1)

		for j := 1; j < i; j++ {
			row = append(row, result[i-1][j-1]+result[i-1][j])
		}

		row = append(row, 1)

		result = append(result, row)
	}

	return result
}
