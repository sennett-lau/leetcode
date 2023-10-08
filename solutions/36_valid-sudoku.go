package solutions

func IsValidSudoku(board [][]byte) bool {
	colMap := make(map[int]bool)
	boxMap := make(map[int]map[byte]bool)

	for i := 0; i < 9; i++ {
		boxMap[i] = make(map[byte]bool)
	}

	for r := 0; r < 9; r++ {
		rowMap := make(map[byte]bool, 9)
		for c := 0; c < 9; c++ {
			if board[r][c] == '.' {
				continue
			}
			if _, ok := rowMap[board[r][c]]; ok {
				return false
			}
			rowMap[board[r][c]] = true

			colIndex := int(board[r][c]) + c*10
			if _, ok := colMap[colIndex]; ok {
				return false
			}
			colMap[colIndex] = true

			boxIndex := r/3*3 + c/3
			if _, ok := boxMap[boxIndex][board[r][c]]; ok {
				return false
			}
			boxMap[boxIndex][board[r][c]] = true
		}
	}
	return true
}
