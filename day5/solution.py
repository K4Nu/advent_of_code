"""part 1
tab=[[] for _ in range(9)]
starter=open("starter.txt").readlines()[:-1]
for line in starter:
    line=line.rstrip()
    for x in range(0,len(line),4):
        if line[x+1].isalpha():
            tab[x//4].insert(0,line[x+1])
with open("d5_1.txt") as file:
    for line in file:
        line=line.rstrip().split(" ")
        move,a,b=int(line[1]),int(line[3]),int(line[5])
        new_tab=tab[a-1][-move:][::-1]
        tab[a-1]=tab[a-1][:-move]
        tab[b-1]+=new_tab
for x in tab:
    print(x[-1],end="")
"""

"""part2
tab=[[] for _ in range(9)]
starter=open("starter.txt").readlines()[:-1]
for line in starter:
    line=line.rstrip()
    for x in range(0,len(line),4):
        if line[x+1].isalpha():
            tab[x//4].insert(0,line[x+1])
with open("d5_1.txt") as file:
    for line in file:
        line=line.rstrip().split(" ")
        move,a,b=int(line[1]),int(line[3]),int(line[5])
        new_tab=tab[a-1][-move:]
        tab[a-1]=tab[a-1][:-move]
        tab[b-1]+=new_tab
for x in tab:
    print(x[-1],end="")
"""