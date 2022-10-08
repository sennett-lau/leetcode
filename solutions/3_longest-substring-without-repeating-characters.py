def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    max = 0
    for i in range(len(s)):
        if len(s) - i < max:
            break
        txt = s[i]
        for j in s[i + 1:]:
            if j not in txt:
                txt += j
            else:
                break
        max = len(txt) if len(txt) > max else max

    return max