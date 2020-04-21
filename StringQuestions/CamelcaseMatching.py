class CamelcaseMatching:
    def camelcaseMatching(self, queries, pattern):
        res = []
        for query in queries:
            res.append(self.isCamelcase(query, pattern))
        return res

    def isCamelcase(self, query, pattern):
        i = 0
        j = 0
        while j < len(pattern):
            # if pattern is still going on but query is finished
            if i >= len(query):
                return False

            # Go through query until matched character is found
            while i < len(query):
                c = query[i]
                # if character is uppercase and doesn't match pattern
                if 'A' <= c <= 'Z' and c != pattern[j]:
                    return False
                # move to next char
                i += 1
                # if current character matches pattern character than break and take next pattern character
                if c == pattern[j]:
                    break

            # move to next pattern char
            if i < len(query):
                j += 1

        # if pattern is not finished
        if j < len(pattern):
            return False

        # if pattern is finished and query is still left, than lookout if there is any uppercase character left
        while i < len(query):
            if 'A' <= query[i] <= 'Z':
                return False
            i += 1

        return True


object = CamelcaseMatching()
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
#print(object.camelcaseMatching(queries, pattern))
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBa"
#print(object.camelcaseMatching(queries, pattern))
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"
#print(object.camelcaseMatching(queries, pattern))

queries = ["IXfGawluvnCa","IsXfGaxwulCa","IXfGawlqtCva","IXjfGawlmeCa","IXfGnaynwlCa","IXfGcamwelCa"]
pattern = "IXfGawlCa"
print(object.camelcaseMatching(queries, pattern))