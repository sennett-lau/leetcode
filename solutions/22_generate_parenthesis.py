class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        def recur(s, l, r):
            if len(s) == n * 2:
                arr.append(''.join(s))
                return
            if l < n:
                s.append('(')
                recur(s, l + 1, r)
                s.pop()
            if r < l:
                s.append(')')
                recur(s, l, r + 1)
                s.pop()

        recur([], 0, 0)

        return arr