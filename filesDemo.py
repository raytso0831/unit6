#Ray Tso
#5/9/18
#fileDemo.py

file=open('engmix.txt')

numWords=0
for line in file:
    if 'ray' in line:
        print(line.strip())
    numWords +=1
    
print(numWords)
