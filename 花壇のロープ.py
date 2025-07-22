def flowers_search(up,down,left,right):
    count = 0
    if up != "#":
        count += 1
    if down != "#":
        count += 1
    if left != "#":
        count += 1        
    if right != "#":
        count += 1   
        
    return count     
    
H,W = map(int,input().split())#花壇の範囲、縦(H)横(W)
flowers = []#花壇の場所

for _ in range(H):#花壇の情報の入力
    flowers.append(list(input()))

rope_index = 0#必要なロープの数

#print(H,W,flowers)
for i in range(H):#花壇を探す
    for j in range(W):
        if flowers[i][j] == "#":
            up = flowers[i-1][j] if i > 0 else "0"
            down = flowers[i+1][j] if i < H-1 else "0"
            left = flowers[i][j-1] if j > 0 else "0"
            right = flowers[i][j+1] if j < W-1 else "0"
            
            rope_index += flowers_search(up,down,left,right)
            
print(rope_index)
# 花壇がある場所を調べる
# その花壇の周りに花壇がないか調べる
# 花壇のないマスをrope_indexに足していく
# 全て調べ終えて終了