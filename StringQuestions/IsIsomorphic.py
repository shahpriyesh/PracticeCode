class IsIsomorphic:
    def isIsomorphic(self, s, t):
        iso1_dict = {}
        iso2_dict = {}

        if len(s) != len(t):
            return False

        for c1, c2 in zip(s, t):
            if c1 in iso1_dict:
                if iso1_dict[c1] is not c2:
                    return False
            if c2 in iso2_dict:
                if iso2_dict[c2] is not c1:
                    return False
            else:
                iso1_dict[c1] = c2
                iso2_dict[c2] = c1

        return True


object = IsIsomorphic()
print(object.isIsomorphic("paper", "title"))
print(object.isIsomorphic("foo", "bar"))
print(object.isIsomorphic("ab", "aa"))