class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        d = {'(': ')', '{': '}', '[': ']'}

        stack = []

        for c in s:
            if len(stack) == 0 or c in d:
                if c not in d:
                    return False
                stack.append(c)
            elif c == d[stack[len(stack) - 1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
