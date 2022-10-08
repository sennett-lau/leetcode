def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """

    r = s[0]
    for i in range(0, len(s)):
        k = 1
        txt = s[i]
        txt2 = None
        if i < len(s) - 1 and s[i] == s[i + 1]:
            txt2 = s[i:i + 2]
            while i - k >= 0 and i + k + 1 < len(s) and s[i - k] == s[i + k + 1]:
                txt2 = s[i - k:i + k + 2]
                k += 1

        k = 1
        while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
            txt = s[i - k:i + k + 1]
            k += 1

        if txt2 is not None and len(txt2) > len(txt):
            txt = txt2

        if len(txt) > len(r):
            r = txt

    return r