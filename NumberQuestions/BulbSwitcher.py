class BulbSwitcher:
    def bulbSwitcher(self, n):
        bulbes = [False]*(n+1)
        for i in range(1, n+1):
            j = 1
            x = i*j
            while x < n+1:
                bulbes[x] = not bulbes[x]
                j += 1
                x = i*j
        return sum(filter(None, bulbes))


object = BulbSwitcher()
print(object.bulbSwitcher(3))
print(object.bulbSwitcher(4))
print(object.bulbSwitcher(9999999))