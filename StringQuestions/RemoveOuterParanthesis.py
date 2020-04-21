class RemoveOuterParantesis:
    def __init__(self):
        pass

    def RemoveOuterParanthesis(self, str):
        start = 0
        open, close = 0, 0
        response = ""

        for idx in range(len(str)):
            if str[idx] == '(':
                open += 1
            else:
                close += 1

            if open == close:
                response += str[start+1: idx]
                open, close = 0, 0
                start = idx + 1

        return response


object = RemoveOuterParantesis()
print(object.RemoveOuterParanthesis("(()())((()()))(())"))