class EvaluateDivision:
    def evaluateDivision(self, equations, values, queries):
        res = []
        # create a map of variables that contains list of possible variable derivations
        varMap = {}
        # for each equation create probable values for each variable in a map
        for i, eq in enumerate(equations):
            var1 = eq[0]
            var2 = eq[1]

            if var1 not in varMap:
                varMap[var1] = [[values[i], var2]]
            else:
                varMap[var1].append([values[i], var2])

            if var2 not in varMap:
                varMap[var2] = [[1 / values[i], var1]]
            else:
                varMap[var2].append([1 / values[i], var1])

        # go through each query and evaluate
        for query in queries:
            res.append(self.evaluateQuery(varMap, query))

        return res

    def evaluateQuery(self, varMap, query):
        # LHS of query
        LHS = query[0]
        # RHS of query
        RHS = [1.0, query[1]]

        if query[0] not in varMap or query[1] not in varMap:
            return -1.0

        # deduce RHS so that it has same variable as LHS
        while LHS not in RHS:
            listOfRelations = varMap[RHS[1]]
            for relation in listOfRelations:
                if LHS in relation:
                    RHS[0] = RHS[0] * ((1 / relation[0]) if relation[0] < 1 else relation[0])
                    RHS[1] = relation[1]
                    break

            if LHS in RHS:
                break

            for relation in listOfRelations:
                RHS[0] = RHS[0] * ((1 / relation[0]) if relation[0] < 1 else relation[0])
                RHS[1] = relation[1]

        return RHS[0]


object = EvaluateDivision()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(object.evaluateDivision(equations, values, queries))