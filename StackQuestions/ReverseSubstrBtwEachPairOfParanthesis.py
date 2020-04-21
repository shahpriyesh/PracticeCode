class ReverseSubstrBtwEachPairOfParanthesis:
    def reverseParanthesis(self, s):
        stack = ['']
        for c in s:
            if c == ')':
                reversed_word = stack.pop()[::-1]
                prev_word = stack.pop()
                stack.append(prev_word + reversed_word)
            elif c == '(':
                stack.append('')
            else:
                stack[-1] = stack[-1] + c
        return stack[-1]


object = ReverseSubstrBtwEachPairOfParanthesis()
print(object.reverseParanthesis("(abcd)"))
print(object.reverseParanthesis("(u(love)i)"))
print(object.reverseParanthesis("(ed(et(oc))el)"))
print(object.reverseParanthesis("a(bcdefghijkl(mno)p)q"))