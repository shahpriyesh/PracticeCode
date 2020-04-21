import collections

class MinimumAddToMakeParanthesisValid:
    def minAdd(self, S):
        stack = []
        count = 0
        for c in S:
            # push open brackets
            if c == '(':
                stack.append('(')
            # try to pop close brackets, if can't than we need an open bracket for this closed one
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        # total = needed close bracket count + all unclosed open brackets still remaining in stack
        return count + len(stack)


object = MinimumAddToMakeParanthesisValid()
print(object.minAdd("())"))
print(object.minAdd("((("))
print(object.minAdd("()"))
print(object.minAdd("()))(("))