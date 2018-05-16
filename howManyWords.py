#Ray Tso
#5/10/18
#howManyWords.py

file=open('engmix.txt')
words=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

numWords = 0
for line in file:
    words[len(line.strip())]+=1

for i in range(0,23):
    print('there is',words[i] ,i,'words',)

