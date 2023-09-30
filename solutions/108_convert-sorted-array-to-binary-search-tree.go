package solutions

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func SortedArrayToBST(nums []int) *TreeNode {
	l := len(nums)

	if l == 0 {
		return nil
	}

	m := l / 2

	root := &TreeNode{Val: nums[m]}
	root.Left = SortedArrayToBST(nums[:m])
	root.Right = SortedArrayToBST(nums[m+1:])

	return root
}
