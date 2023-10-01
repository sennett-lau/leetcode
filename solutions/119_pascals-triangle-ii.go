package solutions

func GetRow(rowIndex int) []int {
	var row []int

	row = append(row, 1)

	for i := 1; i <= rowIndex; i++ {
		num := row[i-1] * (rowIndex - i + 1) / i

		row = append(row, num)
	}

	return row
}
