def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = nums1

    for i in range(len(nums2)):
        m.append(nums2[i])

    m.sort()

    return m[len(m) // 2] if len(m) % 2 > 0 else (m[len(m) // 2] + m[len(m) // 2 - 1]) / 2.0