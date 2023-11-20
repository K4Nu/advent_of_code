h_x,h_y=0,0
t_x,t_y=0,0
tab=[[0,0] for _ in range(9)]
positions=set()
start=(0,0)
directions={"R":(1,0),"D":(0,1),"L":(-1,0),"U":(0,-1)}
with open("d9_1.txt") as file:
    for line in file:
        line=line.rstrip().split()
        d,n=line[0],int(line[1])
        while n>0:
            h_x+=directions[d][0]
            h_y+=directions[d][1]
            """part 1
            if abs(h_x-t_x)>1 or abs(h_y-t_y)>1:
                t_x+=0 if h_x==t_x else (h_x-t_x)/abs(h_x-t_x)
                t_y+=0 if h_y==t_y else (h_y-t_y)/abs(h_y-t_y)
            positions.add((t_x,t_y))
            """
            if abs(h_x-tab[0][0])>1 or abs(h_y-tab[0][1])>1:
                x=0 if h_x==tab[0][0] else (h_x-tab[0][0])/abs(h_x-tab[0][0])
                y=0 if h_x==tab[0][1] else (h_x-tab[0][1])/abs(h_x-tab[0][1])
                tab[0][0]+=x
                tab[0][1]+=y
            positions.add((tab[0][0],tab[0][1]))
            for i in range(1,len(tab)):
                pass
            n-=1
            print(f'head {h_x,h_y} 1 {tab[0][0],tab[0][1]}')
print(len(positions))