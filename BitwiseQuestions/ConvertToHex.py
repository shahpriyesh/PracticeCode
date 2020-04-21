class ConvertToHex:
    def convertToHex(self, num):
        hexmap = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        res = ""
        if num == 0:
            return '0'

        for i in range(8):
            mask = 0xF
            hexDigit = num & mask
            if hexDigit in hexmap:
                res = hexmap[hexDigit] + res
            else:
                res = str(hexDigit) + res
            num = num >> 4
        return res.lstrip('0')


object = ConvertToHex()
print(object.convertToHex(26))
print(object.convertToHex(-1))