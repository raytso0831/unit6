#Ray Tso
#practiceQuiz6.py

#program 1
file=open('engmix.txt')
for line in file:
    if line.count('c')==3 and line.count('p')==2:
        print(line)

