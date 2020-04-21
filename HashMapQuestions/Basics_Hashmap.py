dict = {'a':5, 'b':7, 'c':3}
print(dict.items())

# Find key with minimum value from dictionary
print(min(dict, key=dict.get))