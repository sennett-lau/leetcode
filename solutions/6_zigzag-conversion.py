def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    r = ''

    if numRows == 1:
        return s
    m = 2 * (numRows - 1)
    n = m

    for i in range(numRows):
        c = i
        if (c >= len(s)):
            break
        r += s[c]

        while c < len(s):
            r += s[c + m] if c + m < len(s) else ''
            r += s[c + n] if c + n < len(s) and m != n else ''
            c += n
        m = n if m - 2 == 0 else m - 2

    return r