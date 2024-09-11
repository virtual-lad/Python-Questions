'''Unique in order
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
any elements with the same value next to each other and preserving the original order of elements.

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
'''

def unique_in_order(a):
    output = []
    for i in a:
        if not output or i != output[-1]:
            output.append(i)
    return output

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))

#THE END