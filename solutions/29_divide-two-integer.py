class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_neg = (dividend < 0) ^ (divisor < 0)

        d = abs(dividend)
        s = abs(divisor)

        t = s
        r = 0

        while t <= d:
            c = 1
            while (t << 1) <= d:
                t <<= 1
                c <<= 1
            d -= t
            t = s
            r += c

        return min(2147483647, max(-r if is_neg else r, -2147483648))