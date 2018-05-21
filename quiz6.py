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
    if line[0]==line[4]==line[8]:
        print(line.strip())
        '''
#program 3
file=open('engmix.txt')


