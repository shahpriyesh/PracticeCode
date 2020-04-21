class ValidParanthesis:
    def __init__(self):
        pass

    def isValid(self, s):
        stack = []
        valid_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c is '(' or c is '[' or c is '{':
                stack.append(c)
            elif c is ')' or c is ']' or c is '}':
                if not stack:
                    return False
                last = stack.pop()
                if valid_dict[c] != last:
                    return False

        if stack:
            return False

        return True


object = ValidParanthesis()
s = "()"
print(object.isValid(s))
s = "()[]{}"
print(object.isValid(s))
s = "(]"
print(object.isValid(s))
s = "([)]"
print(object.isValid(s))
s = "{[]}"
print(object.isValid(s))
s = "}"
print(object.isValid(s))