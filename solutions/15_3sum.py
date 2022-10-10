class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        r = []

        for i, t in enumerate(nums):
            d = {}
            if t > 0:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j, v in enumerate(nums[i + 1:]):
                if -1 * (t + v) in d:
                    arr = [t, -1 * (t + v), v]
                    arr.sort()
                    if arr not in r:
                        r.append(arr)
                else:
                    d[v] = j

        return r