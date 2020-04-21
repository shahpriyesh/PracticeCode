# https://leetcode.com/problems/satisfiability-of-equality-equations/
class EqInfo:
    EqList = []
    NotEqList = []
    val = -1

    def __init__(self):
        self.EqList = []
        self.NotEqList = []
        self.val = -1


class EqualityEquations:
    next_num = 1
    dict = {}

    def __init__(self):
        self.next_num = 1
        self.dict = {}

    # doesn't work for case-6
    def equationsPossible_My(self, equations):
        for equation in equations:

            # extract var1 and if not exist in map than add it
            if equation[0] not in self.dict:
                object = EqInfo()
                self.dict[equation[0]] = object

            # extract var2 and if not exist in map than add it
            if equation[3] not in self.dict:
                object = EqInfo()
                self.dict[equation[3]] = object

            # check equality and append proper relation between var1 and var2
            if equation[1] is "=":
                self.dict[equation[0]].EqList.append(equation[3])
            else:
                self.dict[equation[0]].NotEqList.append(equation[3])

        for var, object in self.dict.items():

            # check if variable has not been assigned a value
            if object.val == -1:

                # assign value to variable
                object.val = self.next_num

            # assign value to all variables that are supposed to be equal
            for eqvar in object.EqList:
                # check if the variable which is supposed to be equal already has some unequal value assigned
                if self.dict[eqvar].val != -1 and self.dict[eqvar].val != object.val:
                    return False
                else:
                    self.dict[eqvar].val = object.val

            # assign value to all variables that are supposed to be not equal
            for noteqvar in object.NotEqList:
                # check if the variable which is supposed to be not equal already has equal value assigned
                if self.dict[noteqvar].val != -1 and self.dict[noteqvar].val == object.val:
                    return False
                else:
                    self.next_num += 1
                    self.dict[noteqvar].val = self.next_num

            # use next number for more assignments
            self.next_num += 1

        return True


# case-1
object = EqualityEquations()
equations = ["a==b","b!=a"]
print(object.equationsPossible(equations))

# case-2
object = EqualityEquations()
equations = ["b==a","a==b"]
print(object.equationsPossible(equations))

# case-3
object = EqualityEquations()
equations = ["a==b","b==c","a==c"]
print(object.equationsPossible(equations))

# case-4
object = EqualityEquations()
equations = ["a==b","b!=c","c==a"]
print(object.equationsPossible(equations))

# case-5
object = EqualityEquations()
equations = ["c==c", "b==d", "x!=z"]
print(object.equationsPossible(equations))

# case-6
object = EqualityEquations()
equations = ["c==c","f!=a","f==b","b==c"]
print(object.equationsPossible(equations))
