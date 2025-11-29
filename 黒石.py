def Search(x,y):
    #can_now = 0
    around = [
        [-1,1],[0,1],[1,1],
        [1,0],[1,-1],[0,-1],
        [-1,-1],[-1,0]
        ]
    
    for i,j in around:
        nx,ny = x+i,y+j
        if 0 <= nx < N and 0<= ny < N:
            
            if Board[x+i][y+j] == "W":
                #can_now += Search_same(x,y,i,j)
                if Search_same(x,y,i,j) == 1:
                    return 1
    #return can_now
    return 0
        
def Search_same(x,y,i,j):
    a,b = x+i,y+j
    if not(0 <= a < N and 0<= b < N):
        return 0
    
    if Board[a][b] == "W":
        return Search_same(x+i,y+j,i,j)
    elif Board[a][b] == "B":
        return 1
    else:
        return 0
    
N = int(input())
Board = [list(input()) for _ in range(N)]

can = 0

for y in range(N):
    for x in range(N):
        if Board[x][y] == ".":
            can += Search(x,y)
            
print(can)