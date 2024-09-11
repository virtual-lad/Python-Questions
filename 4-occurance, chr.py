'''You are given a string. Suppose a character 'c' occurs 4 times in the string.
Replace these consecutive occurrences of the character 'c' with (4, c) in the string.'''

given = "111222333333112222"
output = ""
count = 1
for i in range(1, len(given)):
    if given[i] == given[i-1]:
        count = count + 1
    else:
        output = output + f"({count}, {given[i-1]})"
        count = 1 
output = output + f"({count}, {given[-1]})"
print(output)

# THE END