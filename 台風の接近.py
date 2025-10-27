N,M = map(int,input().split()) #N(地図のサイズ),M(通れない降水量)
rain_map = [list(map(int,input().split())) for _ in range(N)]
#print(N,M,rain_map)

success_road = []

for i in range(N):
    for j in range(N):
        if rain_map[j][i] >= M:
            break
        elif j == N-1:
            success_road.append(int(i+1))

if len(success_road) == 0:
    print("wait")
else:
    print(*success_road)