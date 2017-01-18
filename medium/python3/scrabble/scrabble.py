import sys
import math

import operator
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def in_set(letters, word):
    cletters = list(letters)
    for letter in word:
        if letter in cletters:
            cletters.remove(letter)
        else:
            return False
    return True

val = {
    1: ['e','a','i','o','n','r','t','l','s','u'],
    2: ['d','g'],
    3: ['b','c','m','p'],
    4: ['f','h','v','w','y'],
    5: ['k'],
    8: ['j','x'],
    10: ['q','z']
}


words = {}

n = int(input())
for i in range(n):
    w = input()
    words[w] = {"pos": i}
letters = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(words, file=sys.stderr)
    
#remove word cannot match with letters
for word, data in words.items():
    print("%s anagram of %s => %s" % (word, letters, in_set(letters, word)), file=sys.stderr)
    if len(word) > 7 or not in_set(letters, word):
        words[word]['remove'] = True
        continue

        
print(words, file=sys.stderr)

words_val = {}

# count weight scrabble

for word, data in words.items():
    if 'remove' in data and data['remove'] :
        continue
    data['count'] = 0
    for letter in word:
        data['count'] += [k for k, v in val.items() if letter in v][0]
        
    words_val[word] = data

#print(words_val, file=sys.stderr)

# sort
max_count = words_val[max(words_val, key= lambda word: words_val[word]['count'])]['count']
#print(max_count, file=sys.stderr)

words_max = {}

for word, data in words_val.items():
    if data['count'] == max_count:
        print(word, data, file=sys.stderr)
        words_max[word] = data

tab = sorted(words_max, key= lambda word: words_val[word]['pos'])
for key in tab:
    print(key, file=sys.stderr)

if tab:
    print(tab[0])
else:
    print("invalid word")
