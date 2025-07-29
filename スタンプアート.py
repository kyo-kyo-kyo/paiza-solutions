H,W,N = map(int,input().split())#縦の大きさ H 横の大きさ W 個数 N 
stamp = []

for _ in range(N):#スタンプの種類
    s = [input() for _ in range(H)]
    stamp.append(s)


R,C = map(int,input().split())#アートの縦 R 横 C

art = []

for _ in range(R):#アートの配置
    art.append(list(map(int,input().split())))
    
print(H,W,N,stamp,R,C,art)

new_art = []
for i in range(R):
    print(i)
    for v in range(C):
        for j in range(N):
            if art[i][v] == j+1:
                new_art.append(stamp[j])

for r in range(R):
    for h in range(H):
        v = ""
        for c in range(C):
            stamp_index = art[r][c] -1
            v += stamp[stamp_index][h]
        print(v)