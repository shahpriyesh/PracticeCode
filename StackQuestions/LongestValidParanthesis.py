import os
import json
import pprint

class LongestValidParanthesis:
    def longestValidParanthesis(self, s):
        stack = []
        longest = 0
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                # if stack has nothing, this ')' is invalid
                if stack:
                    mid = ""
                    popped = stack.pop()
                    while popped != '(':
                        mid = popped + mid
                        # if stack is now empty than simply push constructed string
                        if not stack:
                            # invalid string is found here, so empty stack
                            longest = max(longest, len(mid))
                            stack = []
                            # stack.append(mid)
                            break
                        # try taking out next entry from stack
                        else:
                            popped = stack.pop()
                    # if we reached here because last popped value was open bracket than construct string and append
                    if popped == '(':
                        stack.append('(' + mid + ')')
                        longest = max(longest, len(mid)+2)

        # if stack has values at end, that means the entire entry in stack is valid parantheses til unclosed open braces
        final = ""
        while stack:
            popped = stack.pop()
            if popped == '(':
                longest = max(longest, len(final))
                final = ""
            else:
                final = popped + final
        longest = max(longest, len(final))

        # valid parantheses length can never be 1
        return longest if longest > 1 else 0


object = LongestValidParanthesis()
print(object.longestValidParanthesis("(()"))
print(object.longestValidParanthesis(")()())"))
print(object.longestValidParanthesis(")()())()()("))
print(object.longestValidParanthesis("("))
print(object.longestValidParanthesis("()()"))
print(object.longestValidParanthesis(")()(((())))("))
print(object.longestValidParanthesis("(())()(()(("))




def FakeOutput():
  filename = os.path.join(
      os.path.dirname(__file__), '/Users/pshah/Downloads/FAKE_OUTPUT.json')
  with open(filename, 'r') as output:
    fake_output = json.load(output)
  return fake_output

print(FakeOutput())
#pprint.pprint(FakeOutput())