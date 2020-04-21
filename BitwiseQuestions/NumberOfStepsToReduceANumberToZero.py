def reduceToZero(num):
    count = 0
    while num:
        if num & 1:
            count += 1
        num >>= 1
        if num:
            count += 1
    return count


print(reduceToZero(14))
print(reduceToZero(8))
print(reduceToZero(123))