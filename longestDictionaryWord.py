#Ray Tso
#5/10/18
#longestDictionaryWord.py

dictionary = open('engmix.txt')

l = 0
word = ""
for h in dictionary:
    lenn = len(h)
    if lenn > l:
        l = lenn
        word = h
print("The longest word is", word)

