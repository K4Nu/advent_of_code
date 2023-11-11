"""day 1 part 1
maxi=curr=0
with open("d1_1.txt") as file:
    for line in file:
        line=line.replace("\n","").split()
        if len(line)>0:
            curr+=int(line[0])
        else:
            maxi=max(maxi,curr)
            curr=0
print(maxi)
"""

"""
day 1 part 2
curr=0
tab=[]
with open("d1_1.txt") as file:
    for line in file:
        line=line.replace("\n","").split()
        if len(line)>0:
            curr+=int(line[0])
        else:
            print(curr)
            tab.append(curr)
            curr=0
tab=sorted(tab)
print(sum(tab[-3:]))
"""