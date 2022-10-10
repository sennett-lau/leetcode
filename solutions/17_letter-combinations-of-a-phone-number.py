class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        r = []

        if len(digits) == 0:
            return r

        self.recur(digits, 0, '', d, r)

        return r

    def recur(self, digits, layer, path, d, r):

        if len(digits) == layer:
            r.append(path)
            return

        for i in d[digits[layer]]:
            self.recur(digits, layer + 1, path + i, d, r)
            