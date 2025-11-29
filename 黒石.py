def Search(x,y):
    can_now = 0
    around = [
        [-1,1],[0,1],[1,1],
        [1,0],[1,-1],[0,-1],
        [-1,-1],[-1,0]
        ]
    for i,j in around:
        if Board[x+i][y+j] == "W":
            
    
N = int(input())
Board = [list(input()) for _ in range(N)]

can = 0

for y in range(N):
    for x in range(N):
        if Board[x][y] == "B":
            can += Search(x,y)