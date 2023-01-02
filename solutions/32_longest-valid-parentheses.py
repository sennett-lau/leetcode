class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]
        ans = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack = stack[:-1]
                if len(stack) > 0:
                    ans = max(ans, i - stack[len(stack) - 1])
                else:
                    stack.append(i)
        return ans
