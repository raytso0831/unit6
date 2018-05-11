#Ray Tso
#5/11/18
#warmup16.py

numWords = 0
file = open('engmix.txt')
for word in file:
    word=word.strip()
    if len(file)<0 and word[0]=='r'and word[-1]=='t':
        print(word.strip())
    numWords += 1
print(numWords)


    
