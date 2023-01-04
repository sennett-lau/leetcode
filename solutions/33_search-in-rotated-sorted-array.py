class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        s, e = 0, len(nums) - 1
        t = target

        while e >= s:
            m = (s + e) / 2

            if nums[m] == t:
                return m

            if nums[s] <= nums[m]:
                if nums[s] <= t <= nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if nums[m] <= t <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1

        return -1
