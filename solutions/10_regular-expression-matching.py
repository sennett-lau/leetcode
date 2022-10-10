class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if len(p) == 0:
            return len(s) == 0

        if len(p) > 1 and p[1] == '*':
            flag = self.isMatch(s, p[2:])
            if flag:
                return True
            for i in range(0, len(s)):
                if s[i] != p[0] and p[0] != '.':
                    return False
                flag = self.isMatch(s[i + 1:], p[2:])
                if flag:
                    return True
        elif len(s) == 0:
            return False
        elif s[0] == p[0] or p[0] == '.':
            return self.isMatch(s[1:], p[1:])

        return False