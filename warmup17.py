#Ray Tso
#5/17/18
#warmup17.py

file = open('engmix.txt')
for line in file:
    if 'r'in line and 'a'in line and 'y' in line and 't' in line and 's' in line and 'o' in line:
        print(line.strip())

