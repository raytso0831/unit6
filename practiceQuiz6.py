#Ray Tso
#practiceQuiz6.py

#program 1
'''
file=open('engmix.txt')
for line in file:
    if line.count('c')==3 and line.count('p')==2:
        print(line)
        '''
'''
#program 2

file=open('engmix.txt')
numWord=0
for line in file:
    if 'r'in line:
        numWord +=1
print('There are' ,numWord, 'words with the letter r')
'''


#program 3
'''
file=open('engmix.txt')
numWord=int(input('Enter a number'))
for line in file:
    if len(line.strip())==numWord:
        print(line.strip())
        break
        '''
'''
#program 4
file=open('engmix.txt')
numWord=0
letter=input('enter a letter')
for line in file:
    if letter not in line:
        numWord +=1
print('There is',numWord,'words without the letter' ,letter, )
'''

'''
#program 5

file=open('engmix.txt')
list=[]
for line in file:
    if line.strip()!="":
        list.append(line.strip())
print(list[len(list)//2-1])
































