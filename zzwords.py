#Ray Tso
#5/10/18
#zzwords.py

dictionary = open('engmix.txt')
for word in dictionary:
    if 'zz' in word:
        print(word.strip())
