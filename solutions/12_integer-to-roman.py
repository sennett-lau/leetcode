def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    r = ''

    k = 0

    s = str(num)

    for c in s:
        if int(c) < 4:
            for i in range(int(c)):
                if len(s) - k == 4:
                    r += 'M'
                elif len(s) - k == 3:
                    r += 'C'
                elif len(s) - k == 2:
                    r += 'X'
                else:
                    r += 'I'
        elif int(c) == 4:
            if len(s) - k == 3:
                r += 'CD'
            elif len(s) - k == 2:
                r += 'XL'
            else:
                r += 'IV'
        elif int(c) < 9:
            if len(s) - k == 3:
                r += 'D'
            elif len(s) - k == 2:
                r += 'L'
            else:
                r += 'V'
            for i in range(int(c) - 5):
                if len(s) - k == 3:
                    r += 'C'
                elif len(s) - k == 2:
                    r += 'X'
                else:
                    r += 'I'
        else:
            if len(s) - k == 3:
                r += 'CM'
            elif len(s) - k == 2:
                r += 'XC'
            else:
                r += 'IX'
        k += 1

    return r