lst = ["amy", "nancy", "jack", "jaikishan"]

print(sorted(lst))
print(sorted(lst, reverse=True))
print(sorted(lst, key=len))
print(sorted(lst, key=len, reverse=True))

lst.sort()
print(lst)
lst.sort(key=len)
print(lst)
lst.sort(reverse=True)
print(lst)
lst.sort(key=len, reverse=True)
print(lst)