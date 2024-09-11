'''Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.'''

def bar():
    a = input('Enter your design: ')
    stack = []
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            else:
                stack.pop()
    return not stack
    
print(bar())

# THE END