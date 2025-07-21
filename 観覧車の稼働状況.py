v = list(map(int,input().split()))
N,M = v[0],v[1]
gondola = []
for _ in range(N):
    gondola.append(int(input()))

peo = []
for _ in range(M):
    peo.append(int(input()))

print(N,M,gondola,peo)

for i in range(M):
    for j in range(N):
        