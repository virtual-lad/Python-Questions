'''You are given words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.'''

a = ['bcdef', 'abcdefg', 'bcde', 'bcdef']

b = set(a)
print(len(b))

word_count = {}
for word in a:
    if word in word_count:
        word_count[word] = word_count[word]+1
    else:
        word_count[word] = 1


printed_words = set()
for word in a:
    if word not in printed_words:
        print(word_count[word], end=" ")
        printed_words.add(word)

# THE END