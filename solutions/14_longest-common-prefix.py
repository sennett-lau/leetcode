def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    r = ''

    for i in range(len(strs[0])):
        for s in strs:
            if i > len(s) - 1 or strs[0][i] != s[i]:
                return r
        r += strs[0][i]

    return r