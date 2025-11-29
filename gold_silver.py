N = int(input())
V = []
for i in range(N):
    V.append(input().split())
    V[i].append(int(V[i][0]) + int(V[i][1]) * 100)
    #print(V)

new_V = sorted(V,key=lambda x: x[2] , reverse=True)

for i in range(N):
    del new_V[i][2]
    print(*new_V[i])

