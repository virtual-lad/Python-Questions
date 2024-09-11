'''
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even,
return the middle 2 characters.'''

a = 'testing'
mid = len(a) // 2
if len(a) % 2 == 0:
    print('The middle chracter is: ', a[mid-1:mid+1])
else:
    print(a[mid])

# THE END