'''Complete the function that accepts a string parameter,
and reverses each word in the string. All spaces in the string should be retained.
"This is an example!" ==> "sihT si na !elpmaxe"

"double  spaces"      ==> "elbuod  secaps"'''

def rev():
    a = input('Give your thoughts: ')
    l = []
    for i in a.split():
        b = ''
        for j in i:
            b = j+b
        l.append(b)
    print(' '.join(l))

rev()

# THE END