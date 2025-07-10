v = list(map(int,input().split()))
N,K = v[0],v[1]

vege = []

for i in range(N):
    vege.append(list(map(int,input().split())))


min_list = []
market_min = []
for i in range(K):
    vege_min = vege[0][i]
    market = 0
    for j in range(N-1):
        if vege_min > vege[j+1][i]:
            vege_min = vege[j+1][i]
            market = j + 1
    
    market_min.append(market)
            

print(len(list(set(market_min))))

