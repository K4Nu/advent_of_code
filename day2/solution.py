bot=["A","B","C"]
player=["X","Y","Z"]
score=0
""" part 1 
with open("d2_1.txt") as file:
    for line in file:
        line=line.split()
        a,b=line[0],line[1]
        if bot.index(a)==player.index(b):
            score+=3
        elif (bot.index(a)+1)%3==player.index(b):
            score+=6
        score+=ord(b)-ord("W")

print(score)
part 2

with open("d2_1.txt") as file:
    for line in file:
        line=line.split()
        a,b=line[0],line[1]
        if b=="X":
            val=player[bot.index(a)-1]
            score+=(ord(val)-ord("W"))
        elif b=="Z":
            curr=6
            val=player[(bot.index(a)+1)%3]
            curr+=ord(val)-ord("W")
            score+=curr
        else:
            curr=3
            curr+=ord(player[bot.index(a)])-ord("W")
            score+=curr
print(score)
"""