file=open('d8_1.txt').readlines()
score1=score2=0
def multiply(arr):
    total=1
    for num in arr:
        total*=num
    return total
for row in range(1,len(file)-1):
    for col in range(1,len(file[0])-2):
        curr=int(file[row][col])
        """part 1
        up=max([int(file[x][col]) for x in range(row-1,-1,-1) if file[x][col].isnumeric()],default=0)
        right=max([int(file[row][x]) for x in range(col+1,len(file[0])-1) if file[row][x].isnumeric()],default=0)
        down=max([int(file[x][col]) for x in range(row+1,len(file)) if  file[x][col].isnumeric()],default=0)
        left=max([int(file[row][x])for x in range(col-1,-1,-1) if file[row][x].isnumeric()],default=0)
        
        if any(curr>val for val in [up,right,down,left]):
            score1+=1
        """
        """part2"""
        directions=[[-1,0],[0,-1],[0,1],[1,0]]
        score = 1
        for x,y in directions:
            dist=0
            curr_x, curr_y = row, col
            curr_x+=x
            curr_y+=y
            while(0<=curr_x<len(file) and 0<=curr_y<len(file[0])-2):
                dist+=1
                curr_x+=x
                curr_y+=y
            score*=dist
        score2=max(score2,score)

print(score2)
#score1+=len(file)*2+(len(file[0])-1)*2-4
