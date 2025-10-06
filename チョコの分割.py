H,W = map(int,input().split())
choco = []
for _ in range(H):
    choco.append(list(map(int,input().split())))

print(H,W,choco)

choco_half = []
flag = True

for i in range(H):#すべての列調べる
    total = sum(choco[i])
    line = total % 2    #列の合計のあまり
    half = total / 2
    if line == 0: #余りが0なら　
    
        for j in range(1,W-1):
            current_sum += choco[i][j]
            if current_sum == half:
    
    else:    
        flag = False
        
if flag == True:
    print("Yes")
    for i in range(H):
        print(f"{choco_half[i]}")
else:
    print("No")