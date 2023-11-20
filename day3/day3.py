t1=[chr(x) for x in range(ord("a"),ord("z")+1)]
t2=[chr(x) for x in range(ord("A"),ord("Z")+1)]
t=t1+t2
score=0
"""part 1
def count_nums(a,b):
    total=0
    for x in set(a):
        if x in b:
           total+=t.index(x)+1
    return total

with open("d3_1.txt") as file:
    for line in file:
        line=line.rstrip()
        a,b=line[:len(line)//2],line[len(line)//2:]
        score+=count_nums(a,b)
print(score)
"""
def check(a,b,c):
    total=0
    for char in set(a):
        if char in b and char in c:
            print(char)
            return t.index(char)+1
    return total
file=open("d3_1.txt").readlines()
for x in range(0,len(file),3):
    a,b,c=file[x].rstrip(),file[x+1].rstrip(),file[x+2].rstrip()
    score+=check(a,b,c)
print(score)