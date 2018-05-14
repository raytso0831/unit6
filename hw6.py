#Ray Tso
#5/14/18
#hw6.py

file=open('engmix.txt')
words=input('enter a word:')
present=False

for list in file:
    if words==list.strip():
        present=True
        print(words,'is in the list')
  
if present==False:
    print(words,'is not in the list')