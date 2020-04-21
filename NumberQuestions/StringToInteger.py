class StringToInteger:
    def __init__(self):
        pass

    def stringToInt(self, str):
        if not str:
            return 0

        idx = 0
        sign = 1
        result = 0
        s_len = len(str)

        while idx < s_len and str[idx] == " ":
            idx = idx + 1

        if idx < s_len:
            if str[idx] == "-":
                sign = -1
                idx = idx + 1
            elif str[idx] == "+":
                sign = +1
                idx = idx + 1
            else:
                pass

        while idx < s_len and "0" <= str[idx] <= "9":
            result = (result * 10) + (ord(str[idx]) - ord("0"))
            idx = idx + 1

        result = result * sign
        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif result < pow(-2, 31):
            return pow(-2, 31)
        else:
            return result


object = StringToInteger()
print(object.stringToInt("42"))
print(object.stringToInt("   -42"))
print(object.stringToInt("4293 with words"))
print(object.stringToInt("words and 987"))
print(object.stringToInt("-91283472332"))
print(object.stringToInt("+1"))