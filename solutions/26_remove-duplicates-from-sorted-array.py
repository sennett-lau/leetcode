class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        counter = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[counter]:
                counter += 1
                nums[counter] = nums[i]

        return counter + 1
