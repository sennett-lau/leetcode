def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    v = {}
    for i, val in enumerate(nums):
        if target - val in v:
            return [v[target - val], i]
        else:
            v[val] = i
