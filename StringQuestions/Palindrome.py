class Palindrome:
    def isValidCaseInsensitive(self, string):
        return string[::-1].lower() == string.lower()

    def isValidWithoutPython(self, string):
        front, rear = 0, len(string)-1
        while front < rear:
            if string[front].lower() != string[rear].lower():
                return False
            front += 1
            rear -= 1
        return True

    def isValidOnlyAlphaNumericIgnoreCase(self, string):
        front, rear = 0, len(string)-1
        while front < rear:
            c1 = string[front].lower()
            if not 'a' <= c1 <= 'z' and not '0' <= c1 <= '9':
                front += 1
                continue

            c2 = string[rear].lower()
            if not 'a' <= c2 <= 'z' and not '0' <= c2 <= '9':
                rear -= 1
                continue

            if c1 != c2:
                return False

            front += 1
            rear -= 1

        return True

object = Palindrome()
#print(object.isValidOnlyAlphaNumericIgnoreCase("A man, a plan, a canal: Panama"))
print(object.isValidOnlyAlphaNumericIgnoreCase("race a car"))