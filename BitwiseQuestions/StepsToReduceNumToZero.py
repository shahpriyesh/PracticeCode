def reduceNumToZero(n):
    steps = 0
    while n > 0:
        if n & 1:
            steps += 2
        else:
            steps += 1
        n = n >> 1
    # why steps - 1? Because when the number reaches 1, despite being odd number, only substracting 1 will suffice
    return steps - 1


print(reduceNumToZero(14))
print(reduceNumToZero(8))
print(reduceNumToZero(123))