N = int(input())
stone = []
center_stone = N+1 / 2
for _ in range(N):
    stone.append(list(map(int,input().split())))
    
#print(N,stone)
remove_s = 0

for i in range(N):
    for j in range(N):
        layer = min(i,j,N-1-i,N-1-j)
        need = layer + 1
        remove_s += stone[i][j] - need
        
print(remove_s)