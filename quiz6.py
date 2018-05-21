#Ray Tso
#5/21/18
#quiz6.py

'''
#program 1
file=open('engmix.txt')
letter=input('enter a letter')
for line in file:
    if line.count(letter)==4:
        print(line.strip())
        '''

'''
#program 2
file=open('engmix.txt')
for line in file:
    if line[0]==line[4] and line[0]==line[8] and line[4]==line[8]:
        print(line.strip())
        '''
        
'''
#program 3
file=open('engmix.txt')
letter=input('eneter a letter')
numWord=int(input('Enter a number'))
for line in file:
    if len(line.strip())==numWord and  letter in line:
        print(line.strip())
        break
        '''
    
'''
#program 4
file=open('filesDemo.py')

for line in file:
    words=line.split()
    if len(words)==10:
    
        print(words[7999])
        '''
    



