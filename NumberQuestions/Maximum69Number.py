class Maximum69Number():
    def max69Num(self, num):
        res = ''
        num = str(num)
        for i, c in enumerate(num):
            if c == '6':
                res += '9'
                break
            res += c

        res += num[i+1:]
        res = int(res)
        return res


object = Maximum69Number()
print(object.max69Num(9669))
print(object.max69Num(9996))
print(object.max69Num(9999))