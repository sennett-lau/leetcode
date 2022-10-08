def myAtoi(self, s):
    """
    :type s: str
    :rtype: int
    """

    r = 0
    isNeg = None

    for c in s:
        if c.isnumeric():
            r *= 10
            r += int(c)
            isNeg = False if isNeg is None else isNeg
        elif isNeg is not None:
            break
        elif c == '+':
            isNeg = False
        elif c == '-':
            isNeg = True
        elif c == ' ':
            continue
        else:
            break

    if isNeg:
        r *= -1

    if r > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif r < -1 * (2 ** 31):
        return -1 * (2 ** 31)
    else:
        return r