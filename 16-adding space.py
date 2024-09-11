'''Split Camel Case
Complete the solution so that the function will break up camel casing, using a space between words.

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identi fier"
""   =>  ""'''

def space(word , position):
    if position < 0 or position > len(word):
        raise ValueError('Wrong number to split it out')
    else:
        return word[:position]+' '+word[position:]
    
example = 'camalcasing'

print(space(example,5))

# THE END