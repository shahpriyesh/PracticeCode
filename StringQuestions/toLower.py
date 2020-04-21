class toLower:
    def __init__(self):
        pass

    def toLowerInBuilt(self, str):
        return str.lower()

    def toLower(self, input):
        response = ""
        for idx in range(len(input)):
            if input[idx] >= 'A' and input[idx] <= 'Z':
                response = response + chr(ord(input[idx]) + 32)
            else:
                response += input[idx]
        return response

    def toLowerPythonic(self, str):
        return "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in str)


object = toLower()
str_to_lower = "Hello"
print(object.toLowerPythonic(str_to_lower))