P = input().split()
N,K = int(P[0]),int(P[1])

#ビンゴカードの数値
bingo = []
for _ in range (N):
    bingo.append(list(map(int,input().split())))
#print(bingo)
#抽選された数値
lottery = list(map(int,input().split()))
#print(lottery)
#一致する数値を-1に書き換え
for i in range (K):
    for j in range (N):
        for v in range(N):
            if lottery[i] == bingo[j][v]:
                bingo[j][v] = 0
#print(bingo)
hit = 0
#横方向のビンゴ判定
for i in range(N):
        "if sum(int(x) for x in bingo[i]) <= 0:"
        if all(x == 0 for x in bingo[i]):
         hit = hit + 1
#print(hit)
T = 0
#縦方向のビンゴ判定
for i in range(N):
    """
    for j in range(N):
        T = T + int(bingo[j][i])
    
    if T <= 0 :
        hit = hit + 1
    
    T = 0
    """
    if all(bingo[j][i] == 0 for j in range(N)):
        hit = hit + 1
#print(hit)
CL = 0

for i in range(N):
    
    CL = CL + int(bingo[i][i])

if CL == 0:
    hit = hit + 1
#print(hit)
CR = 0

for j in range(N):
    L = (N - 1) - j
    CR = CR + int(bingo[j][L])
    
if CR == 0:
    hit = hit + 1
    
print(hit)
# このコードは10問通るように修正済み
# このコードは10問通るように修正済み
#git diff BINGO.py
