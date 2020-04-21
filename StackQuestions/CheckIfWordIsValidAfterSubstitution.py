class CheckIfWordIsValidAfterSubstitution:
    def checkIfWordIsValid(self, S):
        countList = [0] * 3

        if S.find('abc') == -1:
            return False

        for c in S:
            if c == 'a':
                countList[0] += 1
                # at any given point count of 'a's have to be max in string (as we go Left to Right)
                if max(countList) != countList[0]:
                    return False
            elif c == 'b':
                # at any given point count of 'b's have to be lesser or equal than 'a' and greater than 'c'
                countList[1] += 1
                if countList[0] < countList[1] or countList[1] < countList[2]:
                    return False
            elif c == 'c':
                countList[2] += 1
                # at any given point count of 'c's have to be min in string (as we go Left to Right)
                if min(countList) != countList[2]:
                    return False

        # At the end if there are same number of 'a', 'b', and 'c' than string is valid
        return countList[0] == countList[1] == countList[2]


object = CheckIfWordIsValidAfterSubstitution()
print(object.checkIfWordIsValid("abc"))
print(object.checkIfWordIsValid("aabcbc"))
print(object.checkIfWordIsValid("abcabc"))
print(object.checkIfWordIsValid("aabcbc"))
print(object.checkIfWordIsValid("abcabcababcc"))

print(object.checkIfWordIsValid("abccba"))
print(object.checkIfWordIsValid("ab"))
print(object.checkIfWordIsValid("cababc"))
print(object.checkIfWordIsValid("bac"))
print(object.checkIfWordIsValid("abccba"))
print(object.checkIfWordIsValid("cababc"))

# following case failed because not checking sequence abc in string. There has to be one 'abc' in string.
print(object.checkIfWordIsValid("aabbcc"))

# following case doesn't work and that is why you need stack
print(object.checkIfWordIsValid("abacbabcc"))
