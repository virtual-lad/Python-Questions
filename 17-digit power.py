'''Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p.
we want to find a positive integer k, if it exists,
such that the sum of the digits of n taken to the successive powers of p is equal to k * n.'''

def dig_pow(a, b):
    total = 0
    for i, digit in enumerate(str(a)):
        total +=  int(digit) ** (b + i)
    if total % a == 0:
        return total // a 
    else:
        return -1
    
print(dig_pow(695, 2))
print(dig_pow(46288, 3))

# THE END