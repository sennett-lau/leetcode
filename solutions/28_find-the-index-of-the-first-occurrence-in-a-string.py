class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        r = -1

        for i in range(len(haystack)):
            if needle[0] == haystack[i] and len(needle) + i <= len(haystack):
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j]:
                        break
                    elif j == len(needle) - 1 and needle[j] == haystack[i + j]:
                        return i

        return r