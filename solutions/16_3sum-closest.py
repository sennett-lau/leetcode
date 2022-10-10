class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        r = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == target:
                    return target

                if abs(target - s) < abs(target - r):
                    r = s

                if s < target:
                    j += 1
                elif s > target:
                    k -= 1

        return r
