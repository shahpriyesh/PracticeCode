# Reverse a string
string = "abcd"
str_len = len(string)

# Method 1 - slicing
print(string[str_len::-1])
print(string[::-1])

# Method 2 - Loop
reversed_str = ""
for idx in reversed(range(str_len)):
    reversed_str += string[idx]
print(reversed_str)

# Method 3 - Join (With Iterable => reversed)
reversed_str = ''.join(reversed(string))
print(reversed_str)