'''Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result. Note: Numbers can be from 1 to 9. 
So 1 will be the first word (not 0). If the input string is empty, return an empty string. 
The words in the input String will only contain valid consecutive numbers.

"4very H1e P3UBG m5uch likes2"  -->  "H1e likes2 P3UBG 4very m5uch"'''

def sort_string(a):
    words = a.split()
    print(words)
    sort = sorted(words, key=lambda word: int(''.join(filter(str.isdigit, word))))
    
    return ' '.join(sort)

a = "4very H1e P3UBG m5uch likes2"

print(sort_string(a))

# THE END