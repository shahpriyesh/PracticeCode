import collections

class CounterCheck:
    def counterCheck(self, str1, str2):
        x = collections.Counter(str1)
        print(x)
        y = collections.Counter(str2)
        print(y)
        z = x & y
        print(z == x)


object = CounterCheck()
object.counterCheck("apple", "pineapple")
object.counterCheck("apple", "monkey")