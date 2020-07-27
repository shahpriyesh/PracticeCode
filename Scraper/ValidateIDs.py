def validateIDs(ids):
    ids = (map(str.strip, ids))
    nums = (map(str.isdigit, ids))
    return all(nums)


class Request:
    def __init__(self):
        self.request = 200

    def setCode(self, code):
        self.request = code

    def getCode(self):
        return self.request


class ErrorCheck:
    def badRequest(self, code):
        return code


class ABC(Request, ErrorCheck):
    def check(self, ids):
        ids = ids.strip().split(',')
        if validateIDs(ids):
            self.setCode(202)
        else:
            self.request = self.badRequest(400)
        return self.getCode()


def fn1(d1):
    d1['x'] = 1

def fn2():
    d1 = {}
    fn1(d1)
    print(d1)


object = ABC()
print(object.check("123,456"))
print(object.check("123, 456"))
print(object.check("123 456"))
print(object.check("123,456 "))
print(object.check("abra ka dabra"))

print(fn2())