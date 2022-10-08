def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """

    r = 0

    s = 0
    e = len(height) - 1

    while s < e:
        v = (e - s) * min(height[s], height[e])
        r = max(r, v)

        if height[s] > height[e]:
            e -= 1
        elif height[s] < height[e]:
            s += 1
        else:
            s += 1
            e -= 1

    return r