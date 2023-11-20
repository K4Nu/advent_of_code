score1=score2=0
with open("d4_1.txt") as file:
    for line in file:
        line=line.rstrip()
        p1, p2=line.split(",")
        a1, a2=map(int, p1.split("-"))
        b1, b2=map(int, p2.split("-"))
        if a1<=b1 and a2>=b2 or a1>=b1 and b2>=a2:
            score1+=1
        if (a1 or a2) in range(b1,b2+1) or (b1 or b2) in range(a1,a2+1):
            score2+=1
print(f'Answer for part 1 {score1} and the part 2 is equal {score2}')