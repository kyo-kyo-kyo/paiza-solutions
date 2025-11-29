H,W,R,C,T = map(int,input().split())
forest = []
for _ in range(H):
    forest.append(list(input()))
    
#print(H,W,R,C,T,forest)
forest[R-1][C-1] = "B"

directions = [(-1,0),(1,0),(0,-1),(0,1)]

#print(forest)
for _ in range(T):
    new_forest = [row[:] for row in forest]
    
    for i in range(H):
        for j in range(W):
            
            if forest[i][j] == "B":
                
                for dr,dc in directions:
                    ni,nj = i + dr , j +dc
                    if 0 <= ni < H and 0 <= nj < W:
                        if forest[ni][nj] == "#":
                            new_forest[ni][nj] = "B"
                            
                new_forest[i][j] = "A"
                
    forest = new_forest
    
for i in forest:
    print("".join(i))    

"""if forest[i+1][j] == "#" and i+1 < W-1:
                        forest[i+1][j] = "B"
                        forest[i][j] = "A"
                        print(forest,"r")
                    elif forest[i-1][j] == "#" and i-1 > 0:
                        forest[i-1][j] = "B"
                        forest[i][j] = "A"
                        print(forest,"l")
                    elif forest[i][j+1] == "#" and j+1 < H-1:
                        forest[i][j+1] = "B"
                        forest[i][j] = "A"
                        print(forest,"d")
                    elif forest[i][j-1] == "#" and j-1 > 0:
                        forest[i][j-1] = "B"
                        forest[i][j] = "A"
                        print(forest,"u")"""                 