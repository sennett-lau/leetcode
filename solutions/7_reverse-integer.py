def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    r = 0

    tmp = x if x > 0 else x * -1

    while tmp > 0:
        r *= 10
        r += tmp % 10
        tmp = tmp // 10

    if x < 0:
        r *= -1

    if r > 2 ** 31 - 1 or r < -1 * (2 ** 31):
        return 0

    return r