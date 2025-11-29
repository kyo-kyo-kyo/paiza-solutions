H,W = map(int,input().split())
sea_area = [list(map(int,input().split())) for _ in range(H)]
R,C = map(int,input().split())
network = [list(input()) for _ in range(R)]
#print(H,W,sea_area,R,C,network)
max_fish = 0
for h in range(H-R):
    for w in range(W-C):
        catch = 0
        for r in range(R):
            for c in range(C):
                if network[r][c] == "#":
                    catch += sea_area[h+r][w+c]
                    
        max_fish = max(max_fish,catch)
            
print(max_fish)