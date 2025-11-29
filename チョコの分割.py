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
    
"""   
# 入力
H, W = map(int, input().split())
choco = [list(map(int, input().split())) for _ in range(H)]

result = []  # 各行の分け方を保存
possible = True  # 分けられるかどうか

for i in range(H):
    total = sum(choco[i])
    
    # 奇数なら平等に分けられない
    if total % 2 != 0:
        possible = False
        break

    half = total // 2
    current_sum = 0
    split_index = -1

    # 左から順に糖度を足していって、ちょうど半分になる位置を探す
    for j in range(W - 1):  # 最後の列は残さない（空の人が出ないように）
        current_sum += choco[i][j]
        if current_sum == half:
            split_index = j + 1
            break

    # 見つからなければ失敗
    if split_index == -1:
        possible = False
        break
    else:
        result.append("A" * split_index + "B" * (W - split_index))

# 出力
if possible:
    print("Yes")
    for line in result:
        print(line)
else:
    print("No")
"""