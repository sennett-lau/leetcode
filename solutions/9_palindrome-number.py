def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    s = str(x)

    if len(s) % 2 == 0:
        m = len(s) // 2 - 1
        k = 0
        while m - k >= 0:
            if s[m - k] != s[m + 1 + k]:
                return False
            k += 1
    else:
        m = len(s) // 2
        k = 0
        while m - k >= 0 and m + k < len(s):
            if s[m - k] != s[m + k]:
                return False
            k += 1

    return True