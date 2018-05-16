#Ray Tso
#5/16/18
#reverse.py

file=open('lastWordDemo.py')

list=[]
for line in file:
    line=line.strip()
    list.append(line)
list.reverse()

for l in list:
    print(l)
