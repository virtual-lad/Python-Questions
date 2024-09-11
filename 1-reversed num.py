''' Write a function which will take an integer as input and print each digit in a separate line.
You are not allowed to use str or any other method will convert the integer into string.'''

def num_reverse(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = digit
        num = num // 10
        print(reverse)
num_reverse(1101)

# THE END
