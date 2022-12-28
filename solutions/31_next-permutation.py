class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, len(nums)):
                    if nums[i-1] < nums[j]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        return
        nums.reverse()