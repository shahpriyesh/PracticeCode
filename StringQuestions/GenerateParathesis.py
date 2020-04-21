class GenerateParanthesis:
    def __init__(self):
        pass

    def generateParanthesis(self, n):
        if n == 0:
            return []

        resp = []
        curr = ""
        self.generateParanthesisUtil(0, 0, n, resp, curr)
        return resp

    def generateParanthesisUtil(self, open, close, n, resp, curr):
        if open == close == n:
            resp.append(curr)

        if open < n:
            curr = curr + '('
            self.generateParanthesisUtil(open + 1, close, n, resp, curr)
            curr = curr[0: len(curr)-1]

        if close < open:
            curr = curr + ')'
            self.generateParanthesisUtil(open, close + 1, n, resp, curr)
            curr = curr[0: len(curr) - 1]

        return resp


object = GenerateParanthesis()
print(object.generateParanthesis(2))
print(object.generateParanthesis(3))