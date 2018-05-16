#Ray Tso
#5/14/18
#hw6.py

'''
file=open('engmix.txt')
words=input('enter a word:')
present=False

for list in file:
    if words==list.strip():
        present=True
        print(words,'is in the list')
  
if present==False:
    print(words,'is not in the list')
    '''
    
'''
file=open('engmix.txt')
num=int(input('enter a number'))
L=[]
for line in file:
    line=line.strip
    L.append(line)
print(L[num-1])
'''
'''
file=open('lastWordDemo.py')
for line in file:
    print(line.strip()+'!')
'''
file=open('engmix.txt')
letter=input('enter a letter:')
mostchar=''
for line in file:
    line=line.strip()
    if line.count(letter)>most.char.count(letter):
        mostchar=line
print(mostchar)
