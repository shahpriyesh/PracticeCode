class ZigZagConversion:
    def __init__(self):
        pass

    def zigZagConversion(self, s, numRows):
        result = ""
        s_len = len(s)
        map = {}

        if numRows <= 1:
            return s

        for idx in range(numRows):
            map[idx] = ""

        idx = 0
        m, n = 0, 0

        while idx < s_len:

            while idx < s_len and n < numRows:
                map[n] = map[n] + s[idx]
                idx = idx + 1
                n = n + 1

            m = 0
            n = numRows - 2
            while idx < s_len and m < numRows - 1 and n >= 0:
                map[n] = map[n] + s[idx]
                idx = idx + 1
                m = m + 1
                n = n - 1

            n = 1

        for key, val in map.items():
            result += val

        return result


object = ZigZagConversion()
print(object.zigZagConversion("PAYPALISHIRING", 3))
print(object.zigZagConversion("PAYPALISHIRING", 4))
print(object.zigZagConversion("AB", 1))