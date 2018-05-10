#Ray Tso
#5/10/18
#lastwordDemo.py

file=open('filesDemo.py')

for line in file:
    words=line.split()
    if len(words)>0:
        print(words[-1])
    else:
        print()
