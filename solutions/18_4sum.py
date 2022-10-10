class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        r = []

        nums.sort()

        for i, n in enumerate(nums):
            self.threeSum(nums[i+1:], target - n, n, r)


        return r


    def threeSum(self, nums, target, x, r):
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == target and [x, nums[i], nums[j], nums[k]] not in r:
                    r.append([x, nums[i], nums[j], nums[k]])

                if s <= target:
                    j += 1
                elif s > target:
                    k -= 1
